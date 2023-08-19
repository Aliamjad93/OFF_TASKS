# Importing necessary libraries
from tensorflow.keras.models import load_model
import os; os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'
import numpy as np

from .LSTM_Model import Tokenizer

class Controller:
    #Loading Model File
    def __init__(self):
        
        self.tokenizer = Tokenizer.tokenizer
        path="C:/Users/farha/.spyder-py3/Task1/NextWordPred/Controller/"
        self.model = load_model(path+'next_word_predictions.h5')
    
    def Predict_next_words(self,model,tokenizer,text):
        
        # convert the text into numbers. Giving each text a token
        
        sequence = self.tokenizer.texts_to_sequences([text])
        
        sequence = np.array(sequence)
        
        preds = np.argmax(self.model.predict(sequence))

        token = self.tokenizer.word_index
        
        k1 = [key for key,value in token.items() if value==preds]        
        
        return k1[0]
    
    def MakePrediction(self,text):
        
        
        text = text.input_text.split(" ")
        
        text = text[-3:]

        return self.Predict_next_words(self.model,self.tokenizer,text)


# Creating an instance of the 'Controller' class
controller = Controller()
