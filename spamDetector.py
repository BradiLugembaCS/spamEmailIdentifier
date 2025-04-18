import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split

# Function to load and preprocess the SMS spam dataset
def load_data():
    url = "https://raw.githubusercontent.com/justmarkham/pycon-2016-tutorial/master/data/sms.tsv"
    data = pd.read_csv(url, sep='\t', header=None, names=['label','text'])
    data['label'] = data['label'].map({'ham':0, 'spam':1})
    return data

# Transforms text data into TF-IDF features and prepares it for model training.
def train_model(data):
    x = data['text']
    y = data['label']
    vectorizer = TfidfVectorizer()
    x = vectorizer.fit_transform(x)
    








# Entry point of the script: loads and prints the dataset.
if __name__ == "__main__":
    data = load_data()
    print(data)
