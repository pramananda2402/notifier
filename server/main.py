from fastapi import FastAPI, HTTPException
import httpx
import status
import random
import uvicorn
from collections import defaultdict

app = FastAPI()

NEWS_API_URL = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=bcc8ccd488a148b5bbb402e1011098e5"

# Replacing the list with a dictionary for better data management
news_storage = {}  # Dictionary to store news articles with IDs as keys
current_id = 1
notification_dict = defaultdict(int)

@app.get("/")
async def root():    
    return {"message": "Notifier app home page"}

@app.get("/news/fetch")
async def fetch_and_store_news():
    """
    Fetch news from the API and store them in a dictionary with unique IDs.
    """
    global current_id, news_storage
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(NEWS_API_URL)
            response.raise_for_status()
            data = response.json()
        # Clear old news and store new articles with unique IDs
        news_storage.clear()
        for article in data.get("articles", []):
            article_with_id = {
                "title": article.get("title"),
                "description": article.get("description"),
                "content": article.get("content"),
                "url": article.get("url"),
                "source": article.get("source", {}).get("name"),
            }
            news_storage[current_id] = article_with_id
            ranking_value = random.randint(1, 100)
            notification_dict[current_id] = ranking_value
            current_id += 1

        return {"message": "News fetched and stored successfully", "total": len(news_storage)}

    except httpx.HTTPError as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@app.get("/news")
async def get_all_news():
    """
    Retrieve all stored news articles.
    """
    return {"news": news_storage}

@app.get("/news/{id}")
async def get_news_by_id(id: int):
    """
    Retrieve a specific news article by its ID.
    """
    news_item = news_storage.get(id)
    if not news_item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="News not found")
    return news_item

@app.get("/news/{id}/categories")
async def get_news_categories(id: int):
    """
    Placeholder: Retrieve categories for a specific news article.
    """
    news_item = news_storage.get(id)
    if not news_item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="News not found")
    
    categories = ["Technology", "Startup", "Business", "Politics", "Entertainment", "Sports", "Health", "Science", "Travel", "Food"]
    n = random.randint(1, len(categories))
    return {"id": id, "categories": categories[n-4:n]}

@app.get("/news/{id}/ranking")
async def get_news_ranking(id: int):
    """
    Placeholder: Return a ranking for a specific news article.
    """
    news_item = news_storage.get(id)
    if not news_item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="News not found")
    ranking_value =notification_dict[id] 
    return {"id": id, "ranking": ranking_value}

@app.get("/notification")
async def notification():
    """
    Retrieve all notifications.
    """
    sorted_notifications = dict(sorted(notification_dict.items(), key=lambda item: item[1], reverse=True))
    return sorted_notifications

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
