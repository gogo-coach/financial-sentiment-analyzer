import pandas as pd
import matplotlib.pyplot as plt

def visualize_sentiments(csv_path="sentiment_results.csv"):
    df = pd.read_csv(csv_path)
    
    plt.figure(figsize=(10, 6))
    plt.barh(df["headline"], df["compound"], color="skyblue")
    plt.xlabel("Sentiment Score (Compound)")
    plt.title("Sentiment Analysis of Hong Kong Financial Headlines")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    visualize_sentiments()
