import joblib
from dotenv import load_dotenv
import os
from .SVM_Model.SVM_Model import vectorizer,clean_text

class Controller:
    
    def __init__(self):
        load_dotenv(dotenv_path=r"C:\Users\farha\.spyder-py3\Task1\SentimentAnalysis\Controller\src.env")
        model=os.getenv("model")
        self.model=joblib.load(open(model,'rb'))
        
        
        
        
    def MakePrediction(self,text):
        text=text
        text=clean_text(text)
        
        pred_vectors=vectorizer.transform([text])
        return self.model.predict(pred_vectors)[0]
        
    
controller=Controller()
