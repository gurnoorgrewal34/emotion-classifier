import streamlit as st
import pickle

# Load the saved model and vectorizer
model = pickle.load(open('svm_model.pkl', 'rb'))
vectorizer = pickle.load(open('tfidf_vectorizer.pkl', 'rb'))

# Emotion label mapping
emotionlabel_mapping = {
    0: 'sadness',
    1: 'joy',
    2: 'love',
    3: 'anger',
    4: 'fear',
    5: 'surprise'
}

# Emoji dictionary
emoji_dict = {
    'joy': "😊", 'sadness': "😢", 'anger': "😠", 'fear': "😨", 'love': "❤️", 'surprise': "😮"
}

# Title of the app
st.title("Emotion Detector App")
st.write("Type your message, and I will tell you your mood")

# User input box
input_message = st.text_area("Enter your message here:")

# When the button is clicked
if st.button("Detect Emotion"):
    if input_message.strip() == "":
        st.warning("Please enter some text first.")
    else:
        # Vectorize the input message
        A = vectorizer.transform([input_message])
        
        # Predict the emotion (this returns the index)
        prediction = model.predict(A)[0]

        # Map the prediction index to the emotion label
        emotion = emotionlabel_mapping.get(prediction, "Unknown")

        # Display the predicted emotion
        st.success(f"Predicted Emotion: **{emotion}**")

        # Display the corresponding emoji
        st.write("Emotion Emoji:", emoji_dict.get(emotion, "❓"))
