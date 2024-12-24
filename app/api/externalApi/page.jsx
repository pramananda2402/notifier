// pages/news.js
"use client";
import { useEffect, useState } from 'react';

export default function News() {
  const [articles, setArticles] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    async function fetchNews() {
      const apiKey = 'bcc8ccd488a148b5bbb402e1011098e5';
      const query = 'tesla';
      const from = '2024-11-24';
      const sortBy = 'publishedAt';
      const url = `https://newsapi.org/v2/everything?q=${query}&from=${from}&sortBy=${sortBy}&apiKey=${apiKey}`;

      try {
        const response = await fetch(url);
        if (!response.ok) {
          throw new Error(`Error fetching data: ${response.statusText}`);
        }
        const data = await response.json();
        setArticles(data.articles || []);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    }

    fetchNews();
  }, []);

  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error: {error}</p>;

  return (
    <div>
      <h1>Tesla News</h1>
      {articles.map((article, index) => (
        <div key={index} style={{ marginBottom: '20px' }}>
          <h2>{article.title}</h2>
          <p>{article.description}</p>
          <a href={article.url} target="_blank" rel="noopener noreferrer">
            Read more
          </a>
        </div>
      ))}
    </div>
  );
}
