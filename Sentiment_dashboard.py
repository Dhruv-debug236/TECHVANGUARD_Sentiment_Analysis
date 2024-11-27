import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from textblob import TextBlob  # Simple sentiment analysis tool
# Load data
data = pd.read_csv(r"C:/Users/dp439_ykr3dmm/OneDrive/Desktop/New Data.csv")

print(data)
def analyze_sentiment(text):
    analysis = TextBlob(text)
    return analysis.sentiment.polarity

# Apply sentiment analysis
data['Sentiment'] = data['text'].apply(analyze_sentiment)

# Categorize sentiment
data['Sentiment_Label'] = np.where(data['Sentiment'] > 0, 'Positive',
                                   np.where(data['Sentiment'] < 0, 'Negative', 'Neutral'))
sentiment_summary = data['Sentiment_Label'].value_counts()

print(sentiment_summary)
# Pie chart for sentiment distribution
plt.figure(figsize=(8, 6))
colors = ['lightblue', 'lightcoral', 'lightgreen']
sentiment_summary.plot(kind='pie', autopct='%1.1f%%', colors=colors)
plt.title('Sentiment Distribution')
plt.ylabel('')  # Hides the y-label
plt.show()

# Histogram of sentiment scores
plt.figure(figsize=(8, 6))
plt.hist(data['Sentiment'], bins=20, color='purple', edgecolor='black')
plt.title('Sentiment Polarity Scores')
plt.xlabel('Polarity Score')
plt.ylabel('Frequency')
plt.show()


