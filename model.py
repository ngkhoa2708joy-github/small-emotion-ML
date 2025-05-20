# model.py
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib

# Dữ liệu mẫu
X = [
    "I love this!", "So happy today", "This is great!",
    "I feel sad", "Life is hard", "I am depressed",
    "I hate you", "This makes me angry", "I'm furious"
]
y = ["happy", "happy", "happy", "sad", "sad", "sad", "angry", "angry", "angry"]

# Tạo mô hình
model = Pipeline([
    ("vectorizer", CountVectorizer()),
    ("classifier", MultinomialNB())
])

# Train
model.fit(X, y)

# Lưu model
joblib.dump(model, "emotion_model.joblib")
