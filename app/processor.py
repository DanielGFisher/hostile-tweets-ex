import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

class TextProcessor:
    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()
        self.sid = SentimentIntensityAnalyzer()
        with open(r"C:\Users\danie\PycharmProjectsc\hostile-tweets-ex\data\weapons.txt", "r") as f:
            self.weapons_list = [line.strip().lower() for line in f]

    def process(self):
        """
        Process dataframe and return cleaned
        """
        self.df["rarest_word"] = self.df["original_text"].apply(self.rarest_word)
        self.df["sentiment"] = self.df["original_text"].apply(self.get_sentiment)
        self.df["weapons_detected"] = self.df["original_text"].apply(self.detect_weapons)
        return self.df

    def rarest_word(self, text):
        """
        Find the words which appear least and return a list of them
        """
        words = [w.lower() for w in text.split()]
        if not words:
            return []
        counts = {}
        for word in words:
            counts[word] = counts.get(word, 0) + 1
        min_count = min(counts.values())
        rare_words = [word for word, count in counts.items() if count == min_count]
        return rare_words

    def get_sentiment(self, text):
        """
        Find tweet sentiment -
        Positive, neutral, negative
        """
        score = self.sid.polarity_scores(text)["compound"]
        if score >= 0.5:
            return "positive"
        elif score <= -0.5:
            return "negative"
        else:
            return "neutral"

    def detect_weapons(self, text):
        """
        Find weapon mentions in tweets
        """
        text_lower = text.lower()
        for weapon in self.weapons_list:
            if weapon in text_lower:
                return weapon
        return ""
