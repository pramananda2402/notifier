// pages/api/externalapi.js
export default async function handler(req, res) {
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
      res.status(200).json(data);
    } catch (error) {
      res.status(500).json({ error: error.message });
    }
  }
  