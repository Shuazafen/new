from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.CategoryAPIView.as_view(), name='categories'),
    path('blogs/', views.BlogView.as_view(), name='blogs'),
    path('blogs/<str:id>/', views.BlogDetailView.as_view(), name='blog_detail'),
    path('blogs/category/<str:category_id>/', views.BlogByCategory.as_view(), name='blog_by_category'),
    path('blogs/search/', views.BlogSearch.as_view(), name='blog_search'),
    path('blogs/<str:blog_id>/comments/', views.CommentView.as_view(), name='comments'),
    path('comments/<str:id>/', views.CommentView.as_view(), name='comment_detail'),
]