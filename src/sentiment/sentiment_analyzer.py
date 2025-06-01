# src/sentiment/sentiment_analyzer.py

from transformers import AutoTokenizer, AutoModelForSequenceClassification
from transformers import pipeline
import torch

class FinBERTSentimentAnalyzer:
    def __init__(self, model_name="yiyanghkust/finbert-tone"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSequenceClassification.from_pretrained(model_name)
        self.pipeline = pipeline("sentiment-analysis", model=self.model, tokenizer=self.tokenizer)

    def analyze(self, texts):
        results = self.pipeline(texts)
        formatted = []
        for text, result in zip(texts, results):
            formatted.append({
                "text": text,
                "label": result["label"],
                "score": round(result["score"], 4)
            })
        return formatted
