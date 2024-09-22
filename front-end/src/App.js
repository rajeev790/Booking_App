import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Login from './components/Login';
import Signup from './components/Signup';
import BookingForm from './components/BookingForm';
import Navbar from './components/Navbar';
import Footer from './components/Footer';
import './styles/common.css';

const App = () => {
  return (
    <Router>
      <Navbar />
      <main>
        <Routes>
          <Route path="/" element={<h1>Welcome to the Booking System</h1>} />
          <Route path="/login" element={<Login />} />
          <Route path="/signup" element={<Signup />} />
          <Route path="/book" element={<BookingForm />} />
        </Routes>
      </main>
      <Footer />
    </Router>
  );
};

export default App;
