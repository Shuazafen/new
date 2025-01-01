import React, { useState, useEffect } from 'react'
import { FaSearch, FaUser, FaBars} from "react-icons/fa"
import './Navbar.css'
import axios from "axios"
import { Link, useNavigate } from 'react-router-dom'

const Navbar = () => {

    const [list, setList] = useState([]);

    const fetchList = async () => {
        const response = await axios.get(`${url}/api/categories/`);
        if (response.data.success){
            setList(response.data.data);
        }
        else{
            console.log("Error fetching data");
        }
    }

    const url = "http://127.0.0.1:8000"

    const [menu,setMenu] = useState("home");

    const navigate = useNavigate()



    const logout = () => {

    }

    useEffect(() => {
      fetchList();
    }, [])
  return (
    <div className='navbar'>
      <nav className="nav">
        <FaSearch className='search'/>
        <Link to='/'><img src="" alt="Blog logo" className='logo' /></Link>
        <button className='button'><FaUser /> Login</button>
      </nav>

      <hr />


      <div className="cat">
              

              <ul className={`nav-links ${menu === 'categories'? 'active' : ''}`}>
                  {list.map((item) => (
                      <li key={item.id}><Link to={`/category/${item.id}`} onClick={() => setMenu('categories')}>{item.name}</Link></li>
                  ))}
              </ul>

              <ul className="nav-links">
                <li>work</li>
                <li>hello</li>
                <li>slice</li>
                <li>witgh</li>
                <li>slick</li>
              </ul>

      </div>
      
    </div>
  )
}

export default Navbar
