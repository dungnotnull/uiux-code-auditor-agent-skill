import React, { useState } from 'react';

export function CheckoutForm({ onSubmit }) {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    cardNumber: '',
    expiry: '',
    cvv: '',
  });
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [error, setError] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setIsSubmitting(true);
    try {
      await onSubmit(formData);
    } catch (err) {
      setError('Error occurred');
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <div>
      <div>
        <h2>Checkout</h2>
        <form onSubmit={handleSubmit}>
          <div className="flex flex-col gap-4">
            <div>
              <input
                placeholder="Full Name"
                value={formData.name}
                onChange={(e) => setFormData({ ...formData, name: e.target.value })}
                className="border border-gray-300 p-2"
              />
            </div>
            <div>
              <input
                placeholder="Email Address"
                value={formData.email}
                onChange={(e) => setFormData({ ...formData, email: e.target.value })}
                className="border border-gray-300 p-2"
              />
            </div>
            <div>
              <input
                placeholder="Card Number"
                value={formData.cardNumber}
                onChange={(e) => setFormData({ ...formData, cardNumber: e.target.value })}
                className="border border-gray-300 p-2"
              />
            </div>
            <div className="flex gap-4">
              <input
                placeholder="MM/YY"
                value={formData.expiry}
                onChange={(e) => setFormData({ ...formData, expiry: e.target.value })}
                className="border border-gray-300 p-2"
              />
              <input
                placeholder="CVV"
                value={formData.cvv}
                onChange={(e) => setFormData({ ...formData, cvv: e.target.value })}
                className="border border-gray-300 p-2"
              />
            </div>
          </div>
          <button
            type="submit"
            className="bg-blue-500 text-white px-4 py-2"
          >
            Pay Now
          </button>
        </form>
        {error && <div className="text-red-500">{error}</div>}
      </div>
    </div>
  );
}
