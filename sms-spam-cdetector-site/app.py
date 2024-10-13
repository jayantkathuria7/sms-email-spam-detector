import streamlit as st
import pickle
import string
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import sklearn

ps = PorterStemmer()

def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()
    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)


current_dir = os.path.dirname(os.path.abspath(__file__))
vectorizer_path = os.path.join(current_dir, 'vectorizer.pkl')
model_path = os.path.join(current_dir, 'model.pkl')
tfidf = pickle.load(open(vectorizer_path, 'rb'))
model = pickle.load(open(model_path, 'rb'))

st.title("Email/SMS Spam Detector")

input = st.text_input('Enter the message:')

if st.button("Predict"):
    transformed_sms = transform_text(input)
    vector_input = tfidf.transform([transformed_sms])

    result = model.predict(vector_input)[0]

    if result == 1:
        st.header("Spam")
    else:
        st.header("Not Spam")
