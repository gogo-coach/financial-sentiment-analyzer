import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd

# Download once
nltk.download('vader_lexicon')

# Initialize VADER
analyzer = SentimentIntensityAnalyzer()

# Add Hong Kong finance-specific words
hk_custom_words = {
    "property cooling measure": -1.5,
    "stamp duty relief": 1.2,
    "tech crackdown": -1.3,
    "rate hike": -1.2,
    "rate cut": 1.3,
    "bull market": 1.5,
    "bear market": -1.5,
    "IPO frenzy": 1.0,
}

analyzer.lexicon.update(hk_custom_words)

# Load sample news headlines
with open("hk_news_samples.txt", "r", encoding="utf-8") as file:
    headlines = file.readlines()

# Analyze sentiment
results = []
for headline in headlines:
    scores = analyzer.polarity_scores(headline)
    results.append({
        "headline": headline.strip(),
        "positive": scores["pos"],
        "neutral": scores["neu"],
        "negative": scores["neg"],
        "compound": scores["compound"]
    })

# Output results to CSV
df = pd.DataFrame(results)
df.to_csv("sentiment_results.csv", index=False)
print("Sentiment analysis complete. Results saved to sentiment_results.csv.")
