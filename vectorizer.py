import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle

# Step 1: Load the CSV file
file_path = r"C:\Users\dp439_ykr3dmm\OneDrive\Desktop\New Data.csv"  # Replace with the actual path to your CSV file
data = pd.read_csv(file_path)

# Step 2: Extract the text data column
# Replace 'text_column' with the name of the column containing text in your CSV
text_data = data['text']

# Step 3: Initialize and train the vectorizer
vectorizer = TfidfVectorizer()
vectorizer.fit(text_data)

# Save the trained vectorizer to a .pkl file
with open("vectorizer.pkl", "wb") as file:
    pickle.dump(vectorizer, file)

print("Vectorizer trained and saved successfully!")
