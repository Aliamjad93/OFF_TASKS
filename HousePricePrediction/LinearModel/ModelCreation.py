# Importing necessary libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

# Importing the 'load_dotenv' function from the 'dotenv' library to load environment variables
from dotenv import load_dotenv
import os

# Creating a class called 'Controller'
class LinearModel:
    def __init__(self):
        # Load environment variables from .env file
        load_dotenv(dotenv_path="C:/Users/farha/.spyder-py3/Task1/HousePricePrediction/NewTextDocument.env")

        # Access environment variables
        self.path = os.getenv("dataset_path")  # Path to the dataset
        self.model_path = os.getenv("saved_model")  # Path to save the trained model
        self.df = pd.read_csv(self.path)  # Read the dataset into a Pandas DataFrame
    
    def ModelPreprocessing(self):
        # Drop the 'Address' column from the DataFrame
        self.df.drop(['Address'], axis=1, inplace=True)
        self.x = self.df.drop(['Price'], axis=1)  # Features (input) for the model
        self.y = self.df['Price']  # Target variable (output) for the model
    
    def ModelTraining(self):
        # Split the data into training and testing sets
        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(self.x, self.y, test_size=0.2, random_state=0)
        
        # Create a Linear Regression model
        self.model = LinearRegression()
        
        # Train the model on the training data
        self.model.fit(self.x_train, self.y_train)
        
    def Model(self):
        # Save the trained model using the joblib library
        joblib.dump(self.model, 'linear_model.joblib')
        
    def ModelScore(self):
        # Evaluate the model's performance on the test data
        linear_model_score = self.model.score(self.x_test, self.y_test)
        
        # Print the model's score (R-squared value)
        print(linear_model_score)

# End of the Controller class
