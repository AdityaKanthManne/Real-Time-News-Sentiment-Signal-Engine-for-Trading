# src/ingestion/news_api.py

import requests
import datetime

NEWS_API_KEY = "b0bb724177b34954bc78e92412c568e9"
NEWS_API_ENDPOINT = "https://newsapi.org/v2/everything"

def fetch_news(query="bitcoin OR stocks", from_date=None, to_date=None, language="en", page_size=50):
    if not from_date:
        from_date = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d")
    if not to_date:
        to_date = datetime.datetime.now().strftime("%Y-%m-%d")

    params = {
        "q": query,
        "from": from_date,
        "to": to_date,
        "language": language,
        "sortBy": "publishedAt",
        "pageSize": page_size,
        "apiKey": NEWS_API_KEY
    }

    response = requests.get(NEWS_API_ENDPOINT, params=params)
    if response.status_code == 200:
        articles = response.json().get("articles", [])
        return [(article["title"], article["description"]) for article in articles]
    else:
        raise Exception(f"NewsAPI Error {response.status_code}: {response.text}")
