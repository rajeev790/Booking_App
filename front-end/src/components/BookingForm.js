import React, { useState } from 'react';
import './booking.css';

const BookingForm = () => {
  const [bookingDetails, setBookingDetails] = useState({
    date: '',
    type: '',
    details: ''
  });

  const handleChange = (e) => {
    setBookingDetails({
      ...bookingDetails,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // Add booking logic here
  };

  return (
    <div className="booking-container">
      <h2>Book a Trip</h2>
      <form onSubmit={handleSubmit}>
        <label htmlFor="date">Date:</label>
        <input
          type="date"
          id="date"
          name="date"
          value={bookingDetails.date}
          onChange={handleChange}
          required
        />
        <label htmlFor="type">Booking Type:</label>
        <select
          id="type"
          name="type"
          value={bookingDetails.type}
          onChange={handleChange}
          required
        >
          <option value="">Select</option>
          <option value="railway">Railway</option>
          <option value="hotel">Hotel</option>
          <option value="trip">Trip</option>
          <option value="metro">Metro</option>
        </select>
        <label htmlFor="details">Details:</label>
        <textarea
          id="details"
          name="details"
          value={bookingDetails.details}
          onChange={handleChange}
          required
        />
        <button type="submit">Submit</button>
      </form>
    </div>
  );
};

export default BookingForm;
