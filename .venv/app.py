from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd

file=open("my_script.pkl","rb")
model=pickle.load(file)


file2=open("vectorizer.pkl","rb")
vectorizer=pickle.load(file2)
# Load pre-trained model and vectorizer
#with open("my_script.pkl", "rb") as file:
 #   model = pickle.load(file)

#with open("vectorizer.pkl", "rb") as file:
    #vectorizer = pickle.load(file)

# Initialize Flask app
app = Flask(__name__)

# Text cleaning function
def clean_text(text):
    import re
    text = re.sub(r"http\S+", "", text)  # Remove URLs
    text = re.sub(r"[^\w\s]", "", text) # Remove punctuation
    return text.lower()

# Home route
@app.route("/")
def home():
    return render_template("index.html")

# Prediction route
@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        text = request.form["text"]
        cleaned_text = clean_text(text)
        vectorized_text = vectorizer.transform([cleaned_text])
        prediction = model.predict(vectorized_text)
        sentiment_map = {0: "Negative", 1: "Positive", 2: "Neutral"}
        result = sentiment_map[prediction]
        return jsonify({"sentiment": result})

# Batch processing route
@app.route("/batch", methods=["POST"])
def batch():
    file = request.files["file"]
    if file:
        data = pd.read_csv(file)
        data["cleaned_text"] = data["text"].apply(clean_text)
        vectorized_data = vectorizer.transform(data["cleaned_text"])
        predictions = model.predict(vectorized_data)
        sentiment_map = {0: "Negative", 1: "Positive", 2: "Neutral"}
        data["Predicted Sentiment"] = [sentiment_map[pred] for pred in predictions]
        return data.to_json(orient="records")
    return jsonify({"error": "File upload failed"})

if __name__ == "__main__":
    app.run(debug=True)
