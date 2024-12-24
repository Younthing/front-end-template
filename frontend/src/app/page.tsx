'use client';
import { useEffect, useState } from "react";

export default function Home() {
  const [message, setMessage] = useState("");
  const [error, setError] = useState("");

  useEffect(() => {
    const fetchData = async () => {
      try {
        const res = await fetch('/api/hello');
        if (!res.ok) throw new Error('请求失败');
        const data = await res.json();
        setMessage(data.message);
      } catch (err) {
        setError(err instanceof Error ? err.message : '发生未知错误');
        console.error('Error fetching data:', err);
      }
    };
    
    fetchData();
  }, []);

  const handleClick = () => {
    console.log(message);
  };

  return (
    <div className="grid grid-rows-[20px_1fr_20px] items-center justify-items-center min-h-screen p-8 pb-20 gap-16 sm:p-20 font-[family-name:var(--font-geist-sans)]">
      <h1 className="text-4xl font-bold text-center">Welcome to your Geist project!</h1>
      {error ? (
        <p className="text-red-500">{error}</p>
      ) : (
        <p className="text-center">{message}</p>
      )}
      <button 
        onClick={handleClick}
        className="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600"
      >
        打印消息
      </button>
    </div>
  );
}
