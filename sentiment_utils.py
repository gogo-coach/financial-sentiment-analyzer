from nltk.sentiment.vader import SentimentIntensityAnalyzer
from load_lexicon import load_custom_lexicon

def get_analyzer_with_custom_lexicon():
    analyzer = SentimentIntensityAnalyzer()
    custom_lexicon = load_custom_lexicon()
    analyzer.lexicon.update(custom_lexicon)
    return analyzer

def analyze_headlines(headlines, analyzer):
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
    return results
