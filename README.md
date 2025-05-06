# Emotion Classifier App 😄😢😡

This is a machine learning project to classify emotions from text using Logistic Regression, Random Forest, and SVM models.

## 🔍 Project Features

- Classifies text into emotions: joy, sadness, anger, surprise, love, and fear.
- Trained on the `dair-ai/emotion` dataset from Hugging Face
- Uses `TfidfVectorizer` and `SVC`
- Final model accuracy: **88% on test data**
- Streamlit web app interface 

## 📁 Files in This Repo

- `emotion_dataset_train.csv`, `validation.csv`, `test.csv`: dataset files
- `svm_model.pkl`: trained model file
- `tfidf_vectorizer.pkl`: saved vectorizer
- `app.py`: Streamlit app
- `requirements.txt`: dependencies
- `notebook.ipynb`: training and evaluation code 

## 🚀 How to Run It Locally

1. Clone this repo  

git clone https://github.com/gurnoorgrewal34/emotion-classifier.git
cd emotion-classifier

## How to run Streamlit file
streamlit run emotion_app.py  or python -m streamlit run emotion_app.py
