import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

from dotenv import load_dotenv
import os

# Load environment variables from .env file







class Controller:
    def __init__(self):
        load_dotenv(dotenv_path="C:/Users/farha/.spyder-py3/Task1/HousePricePrediction/NewTextDocument.env")
        # self.path= os.getenv("dataset_path")
        # print('\n',self.path)
        # Access environment variables
        self.path= os.getenv("dataset_path")
        self.model_path = os.getenv("saved_model")
        self.df=pd.read_csv(self.path)
        
        # self.df=pd.read_csv(r'C:\Users\farha\.spyder-py3\Task1\HousePricePrediction\USA_Housing.csv')
    
    
    def ModelPreprocessing(self):
        self.df.drop(['Address'],axis=1,inplace=True)
        self.x=self.df.drop(['Price'],axis=1)
        self.y=self.df['Price']
    
    
    def ModelTraining(self):
        self.x_train,self.x_test,self.y_train,self.y_test=train_test_split(self.x,self.y,test_size=0.2,random_state=0)
        self.model=LinearRegression()
        self.model.fit(self.x_train,self.y_train)
        
    
    def Model(self):
        joblib.dump(self.model, 'linear_model.joblib')
        
    def ModelScore(self):
        linear_model=self.model.score(self.x_test,self.y_test)
        print(linear_model)
        
    def MakePrediction(self,income,age,rooms,baths,population):
    
        self.income=income
        self.age=age
        self.rooms=rooms
        self.baths=baths
        self.population=population
        # Load the saved model
        self.loaded_model = joblib.load('linear_model.joblib')


        # Make predictions using the loaded model
        print(self.income,self.age,self.rooms)

        
        predicted=self.loaded_model.predict(np.array([self.income,self.age,self.rooms,self.baths,self.population]).reshape(1,-1))
        
        # predicted=self.model.predict(np.array([self.income,self.age,self.rooms,self.baths,self.population]).reshape(1,-1))
                
        
        
        return {'Predicted Price': predicted[0]}
        
        
controller=Controller()
# controller.ModelPreprocessing()
# controller.ModelTraining()
# controller.Model()
# controller.ModelScore()