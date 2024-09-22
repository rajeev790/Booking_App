import React from 'react';
import { Link } from 'react-router-dom';
import './common.css';

const Navbar = () => {
  return (
    <nav className="navbar">
      <Link to="/">Home</Link>
      <Link to="/login">Login</Link>
      <Link to="/signup">Signup</Link>
      <Link to="/book">Book</Link>
    </nav>
  );
};

export default Navbar;
