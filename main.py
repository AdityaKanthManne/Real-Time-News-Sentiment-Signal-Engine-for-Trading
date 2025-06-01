# main.py

from src.ingestion.news_api import fetch_news
from src.sentiment.sentiment_analyzer import FinBERTSentimentAnalyzer
from src.signals.signal_generator import SignalGenerator
import pandas as pd

def main():
    print("🔄 Fetching latest financial news...")
    headlines = fetch_news(query="bitcoin OR stock OR interest rates", page_size=25)

    texts = [title for title, desc in headlines if title]  # Use title only
    print(f"✅ Retrieved {len(texts)} headlines.\n")

    print("🧠 Analyzing sentiment using FinBERT...")
    sentiment_model = FinBERTSentimentAnalyzer()
    sentiment_results = sentiment_model.analyze(texts)

    print("📊 Generating trade signals...")
    signal_engine = SignalGenerator()
    signals_df = signal_engine.generate_signals(sentiment_results)

    print("📥 Final Signals:\n")
    print(signals_df[["text", "sentiment", "score", "signal"]])

    # Optional: Save to CSV
    signals_df.to_csv("sentiment_signals.csv", index=False)
    print("\n💾 Saved output to sentiment_signals.csv")

if __name__ == "__main__":
    main()
