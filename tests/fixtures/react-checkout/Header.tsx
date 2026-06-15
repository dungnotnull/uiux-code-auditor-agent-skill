import React from 'react';

export function Header() {
  return (
    <header className="bg-white shadow">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between h-16">
          <div className="flex items-center">
            <img src="/logo.png" />
            <nav className="ml-10 flex items-center space-x-4">
              <a href="/" className="text-gray-900">Home</a>
              <a href="/products" className="text-gray-500">Products</a>
              <a href="/about" className="text-gray-500">About</a>
              <a href="/contact" className="text-gray-500">Contact</a>
            </nav>
          </div>
          <div className="flex items-center">
            <button className="text-gray-500">
              <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 100 4 2 2 0 000-4z" />
              </svg>
            </button>
          </div>
        </div>
      </div>
    </header>
  );
}
