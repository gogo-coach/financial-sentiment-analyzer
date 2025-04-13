# Financial Sentiment Analyzer (Hong Kong News Edition)

A lightweight sentiment analysis tool for parsing and scoring Hong Kong-specific financial news.  
This project customizes the VADER lexicon to include region-specific financial terms such as "rate hike", "stamp duty relief", and "tech crackdown".

## Features
- Localized sentiment scoring using financial keywords
- CSV export of analyzed news
- Easy to expand for more custom keywords

## Usage
```bash
pip install -r requirements.txt
python sentiment_analyzer.py
