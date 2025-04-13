import unittest
from sentiment_utils import get_analyzer_with_custom_lexicon

class TestSentimentAnalyzer(unittest.TestCase):

    def setUp(self):
        self.analyzer = get_analyzer_with_custom_lexicon()

    def test_positive_sentiment(self):
        score = self.analyzer.polarity_scores("stamp duty relief boosts buyer confidence")
        self.assertGreater(score['compound'], 0)

    def test_negative_sentiment(self):
        score = self.analyzer.polarity_scores("tech crackdown hits investor morale")
        self.assertLess(score['compound'], 0)

if __name__ == '__main__':
    unittest.main()
