import React, { useState, useEffect } from 'react';
import { fetchCartItems, fetchShippingOptions } from '../api/cart';
import { CheckoutForm } from './CheckoutForm';
import { ShippingMethod } from './ShippingMethod';
import { OrderSummary } from './OrderSummary';

export function CheckoutFlow() {
  const [step, setStep] = useState(1);
  const [cartItems, setCartItems] = useState([]);
  const [shippingOptions, setShippingOptions] = useState([]);
  const [selectedShipping, setSelectedShipping] = useState(null);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    const loadData = async () => {
      try {
        const items = await fetchCartItems();
        const shipping = await fetchShippingOptions();
        setCartItems(items);
        setShippingOptions(shipping);
      } catch (err) {
        console.error('Failed to load checkout data', err);
      } finally {
        setIsLoading(false);
      }
    };
    loadData();
  }, []);

  const handlePlaceOrder = async (formData) => {
    const response = await fetch('/api/orders', {
      method: 'POST',
      body: JSON.stringify({ ...formData, shipping: selectedShipping }),
    });
    if (!response.ok) {
      throw new Error('Order failed');
    }
    return response.json();
  };

  if (isLoading) {
    return <div>Loading...</div>;
  }

  return (
    <div className="min-h-screen bg-white">
      <div className="max-w-4xl mx-auto p-6">
        <h1 className="text-2xl font-bold mb-8">Checkout</h1>

        <div className="mb-6">
          <div className="flex items-center gap-2">
            <span className={step >= 1 ? 'text-blue-500' : 'text-gray-300'}>Cart</span>
            <span className="text-gray-400">→</span>
            <span className={step >= 2 ? 'text-blue-500' : 'text-gray-300'}>Shipping</span>
            <span className="text-gray-400">→</span>
            <span className={step >= 3 ? 'text-blue-500' : 'text-gray-300'}>Payment</span>
          </div>
        </div>

        {step === 1 && (
          <div>
            <h2 className="text-xl mb-4">Your Cart</h2>
            {cartItems.map((item) => (
              <div key={item.id} className="flex justify-between py-2 border-b">
                <span>{item.name}</span>
                <span>${item.price}</span>
              </div>
            ))}
            <button onClick={() => setStep(2)} className="mt-4 bg-blue-500 text-white px-6 py-2">
              Continue to Shipping
            </button>
          </div>
        )}

        {step === 2 && (
          <div>
            <h2 className="text-xl mb-4">Shipping Method</h2>
            {shippingOptions.map((option) => (
              <div key={option.id} className="border p-4 mb-2">
                <input
                  type="radio"
                  name="shipping"
                  value={option.id}
                  onChange={() => setSelectedShipping(option)}
                />
                <span className="ml-2">{option.name} - ${option.price}</span>
              </div>
            ))}
            <button onClick={() => setStep(3)} className="mt-4 bg-blue-500 text-white px-6 py-2">
              Continue to Payment
            </button>
          </div>
        )}

        {step === 3 && (
          <div>
            <h2 className="text-xl mb-4">Payment Details</h2>
            <CheckoutForm onSubmit={handlePlaceOrder} />
          </div>
        )}
      </div>
    </div>
  );
}
