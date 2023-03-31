from administrative_functions.translate import translate
import re
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords



nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')

stop_words = stopwords.words("english")

lemmatizer = WordNetLemmatizer()


def clean_data(text):
    text = re.sub(r'\W', ' ', text)
    text = re.sub(r'[0-9]', ' ', text)
    text = re.sub(r'\s+',' ', text)
    text = translate(text)
    text = text.lower()
    text = re.sub(r'\W', ' ', text)
    text = re.sub(r'[0-9]', ' ', text)
    text = re.sub(r'\s+',' ', text)
    word_list = nltk.word_tokenize(text)
    word_list = [lemmatizer.lemmatize(word) for word in word_list]
    word_list = list(set(word_list))
    word_list = [word for word in word_list if word not in stop_words]

    return word_list




