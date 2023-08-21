import joblib
from dotenv import load_dotenv
import os
from .SVM_Model.SVM_Model import vectorizer, clean_text

class Controller:
    def __init__(self):
        # Load environment variables from the specified file
        load_dotenv(dotenv_path=r"C:\Users\farha\.spyder-py3\Task1\SentimentAnalysis\Controller\src.env")
        # Get the model file path from environment variables
        model = os.getenv("model")
        # Load the pre-trained model using joblib
        self.model = joblib.load(open(model, 'rb'))
        
    def MakePrediction(self, text):
        # Clean the input text
        text = clean_text(text)
        
        # Transform the cleaned text into a vector using the vectorizer
        pred_vectors = vectorizer.transform([text])
        
        # Perform prediction using the loaded model and return the result
        return self.model.predict(pred_vectors)[0]

# Create an instance of the Controller class
controller = Controller()
