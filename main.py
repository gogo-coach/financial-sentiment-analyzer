from sentiment_utils import get_analyzer_with_custom_lexicon, analyze_headlines
import pandas as pd

def main():
    print("🔍 Loading analyzer with Hong Kong-specific financial lexicon...")
    analyzer = get_analyzer_with_custom_lexicon()

    print("📰 Reading headlines from 'hk_news_samples.txt'...")
    with open("hk_news_samples.txt", "r", encoding="utf-8") as f:
        headlines = f.readlines()

    print("💬 Analyzing sentiment of headlines...")
    results = analyze_headlines(headlines, analyzer)

    print("📄 Saving results to 'sentiment_results.csv'...")
    df = pd.DataFrame(results)
    df.to_csv("sentiment_results.csv", index=False)

    print("✅ Sentiment analysis complete. You can now run 'visualize_sentiment.py' to view the chart.")

if __name__ == "__main__":
    main()
