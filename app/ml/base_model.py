import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import json
import re
import os

class DynamicModel:
    def __init__(self, json_file='app/ml/base_model.json'):
        # Load the JSON file into a dictionary
        if os.path.exists(json_file):
            with open(json_file, 'r', encoding='utf-8') as file:
                self.label_dict = json.load(file)
        else:
            self.label_dict = {}
        
        # Convert the dictionary to a DataFrame
        self.data = pd.DataFrame(list(self.label_dict.items()), columns=['query', 'label'])
        self.vectorizer = None
        self.model = None
        self.train_model()

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

    def train_model(self):
        # Train the model if data exists
        if not self.data.empty:
            self.vectorize_text_data()
            self.split_the_data_into_training()
            self.model = SVC(kernel='linear', probability=True)
            self.model.fit(self.X_train, self.y_train)
            self.evaluate_model()
        else:
            print("No data available to train the model.")

    def evaluate_model(self):
        # Evaluate the model
        if self.model:
            self.y_pred = self.model.predict(self.X_test)
            print(f'Accuracy: {accuracy_score(self.y_test, self.y_pred)}')
        else:
            print("Model is not trained yet.")

    def find_label(self, query):
        # Function to find the label using the rule-based system
        for keyword, label in self.label_dict.items():
            if keyword in query:
                return label

    def search(self, query):
        # If no match, use the ML model
        label = self.find_label(query)
        if label:
            return label
        elif self.model:
            query_vectorized = self.vectorizer.transform([query])
            predicted_label = self.model.predict(query_vectorized)[0]
            return predicted_label
        else:
            return "Unknown"

    def add_to_training_data(self, query, label):
        # Add new query and label to the training data
        self.label_dict[query] = label
        self.data = pd.DataFrame(list(self.label_dict.items()), columns=['query', 'label'])
        self.train_model()

    def save_model(self, json_file='base_model.json'):
        # Save the model to a JSON file
        with open(json_file, 'w', encoding='utf-8') as file:
            json.dump(self.label_dict, file, ensure_ascii=False, indent=4)

    # test model:
    def test(self):
        query = input("سوال بپرس: ")
        result = self.search(query)
        print(f'درخواست: {result}')

        # Optionally, ask for feedback
        feedback = input("آیا این پاسخ درست است؟ (بله/خیر): ")
        if feedback.lower() == 'خیر':
            correct_label = input("لطفاً برچسب صحیح را وارد کنید: ")
            self.add_to_training_data(query, correct_label)
            self.save_model()
