# src/signals/signal_generator.py

import pandas as pd

class SignalGenerator:
    def __init__(self, buy_threshold=0.85, sell_threshold=0.85):
        self.buy_threshold = buy_threshold
        self.sell_threshold = sell_threshold

    def generate_signals(self, sentiment_data):
        """
        Input: List of dicts with "text", "label", "score"
        Output: DataFrame with signal tags
        """
        data = []
        for entry in sentiment_data:
            label = entry["label"]
            score = entry["score"]
            signal = "HOLD"

            if label == "positive" and score >= self.buy_threshold:
                signal = "BUY"
            elif label == "negative" and score >= self.sell_threshold:
                signal = "SELL"

            data.append({
                "text": entry["text"],
                "sentiment": label,
                "score": score,
                "signal": signal
            })

        return pd.DataFrame(data)
