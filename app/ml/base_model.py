import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import json
import re

class BasicModel:
    def __init__(self, json_file='base_model.json'):
        # Load the JSON file into a dictionary
        with open(json_file, 'r', encoding='utf-8') as json_file:
            self.label_dict = json.load(json_file)
        
        # Convert the dictionary to a DataFrame
        self.data = pd.DataFrame(list(self.label_dict.items()), columns=['query', 'label'])

        self.set_data_query()

    def preprocess_text(self, text):
        # Preprocess the text data
        text = re.sub(r'\s+', ' ', text)
        return text

    def set_data_query(self):
        # set data query
        self.data['query'] = self.data['query'].apply(self.preprocess_text)

    def vectorize_text_data(self):
        # Vectorize the text data
        self.vectorizer = TfidfVectorizer(ngram_range=(1, 2))
        self.X = self.vectorizer.fit_transform(self.data['query'])
        self.y = self.data['label']

    def split_the_data_into_training(self):
        # Split the data into training and testing sets
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=0.2, random_state=42)

    def train_svm_model(self):
        # Train an SVM model
        self.model = SVC(kernel='linear', probability=True)
        self.model.fit(self.X_train, self.y_train)

    def evaluate_model(self):
        # Evaluate the model
        self.y_pred = self.model.predict(self.X_test)
        print(f'Accuracy: {accuracy_score(self.y_test, self.y_pred)}')

    def find_label(self, query):
        # Function to find the label using both rule-based and ML model
        # Rule-based system (prioritize 'سوالات متداول' matches)
        for keyword, label in self.label_dict.items():
            if keyword in query:
                return label
        
    def search(self, query):
        # If no match, use the ML model
        query_vectorized = self.vectorizer.transform([query])
        predicted_label = self.model.predict(query_vectorized)[0]
        return predicted_label

# Example usage:
model = BasicModel()
model.vectorize_text_data()
model.split_the_data_into_training()
model.train_svm_model()
model.evaluate_model()

while 1:
    # Test with a sample query
    query = input("سوال بپرس: ")
    print(f'درخواست: {model.search(query)}')
