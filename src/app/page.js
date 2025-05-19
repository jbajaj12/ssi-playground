// --- app/page.js ---
'use client';

import { useState } from 'react';

export default function Home() {
  const [message, setMessage] = useState('');

  const callApi = async (endpoint) => {
    try {
      const res = await fetch(`/api/${endpoint}`);
      const data = await res.json();
      setMessage(data.message || 'Success');
    } catch (err) {
      setMessage('Error occurred');
    }
  };

  return (
    <main className="flex min-h-screen flex-col items-center justify-center gap-4 p-8">
      <h1 className="text-2xl font-bold">Datadog APM Demo</h1>

      <button
        onClick={() => callApi('slow')}
        className="p-2 bg-blue-500 text-white rounded"
      >
        Trigger Slow API
      </button>

      <button
        onClick={() => callApi('chain')}
        className="p-2 bg-green-500 text-white rounded"
      >
        Trigger Chained API
      </button>

      <button
        onClick={() => callApi('error')}
        className="p-2 bg-red-500 text-white rounded"
      >
        Trigger Error API
      </button>

      <p className="mt-4 text-lg">{message}</p>
    </main>
  );
}
