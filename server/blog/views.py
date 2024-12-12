from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Blog, Comment, Category
from .serializer import BlogSerializer, CommentSerializer, CategotySerializer
from rest_framework import status
from django.db.models import Q
from rest_framework import authentication, permissions
# Create your views here.

class CategoryAPIView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategotySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BlogView(APIView):
    

    def get(self, request):
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class BlogDetailView(APIView):
    def get_by_id(self, id):
        try:
            return Blog.objects.get(id=id)
        except Blog.DoesNotExist:
            return Http404("product not found")
        
    def get(self, request, id):
        blog = self.get_by_id(id)
        serializer = BlogSerializer(blog)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, id:str):
        blog = self.get_by_id(id)
        blog.delete()
        return Response({"message": "Blog deleted successfully"}, status=status.HTTP_200_OK)
    
class BlogByCategory(APIView):
    def get(self, request, category_id:str):
        try:
            category = Category.objects.get(id=category_id)
            blogs = Blog.objects.filter(category=category)
            serializer = BlogSerializer(blogs, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Category.DoesNotExist:
            return Response({"message": "Category not found"}, status=status.HTTP_404_NOT_FOUND)
    

class BlogSearch(APIView):
    def post(self, request):
        query = request.data.get('query', '')
        if query:
            search_results = Blog.objects.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query)
            )
            search_results = search_results.order__by("id")
            serializer = BlogSerializer(search_results, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"message": "No results found"}, status=status.HTTP_404_NOT_FOUND)
    

class CommentView(APIView):
    def get(self, request, blog_id:str):
        try:
            blog = Blog.objects.get(id=blog_id)
            comments = Comment.objects.filter(blog=blog)
            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Blog.DoesNotExist:
            return Response({"message": "Blog not found"}, status=status.HTTP_404_NOT_FOUND)
        
    def post(self, request, blog_id:str):
        try:
            blog = Blog.objects.get(id=blog_id)
            serializer = CommentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(blog=blog, created_by=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Blog.DoesNotExist:
            return Response({"message": "Blog not found"}, status=status.HTTP_404_NOT_FOUND)
        


    
