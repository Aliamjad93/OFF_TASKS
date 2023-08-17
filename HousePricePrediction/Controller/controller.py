# Importing the necessary libraries
import joblib  # Required for loading the saved model
import numpy as np  # Required for data manipulation

# Creating a class called 'Controller'
class Controller:
    def MakePrediction(self, income, age, rooms, baths, population):
        # Assigning the input parameters to class attributes
        self.income = income
        self.age = age
        self.rooms = rooms
        self.baths = baths
        self.population = population
        
        # Load the saved model using joblib
        self.loaded_model = joblib.load('linear_model.joblib')
        
        # Displaying input values for validation
        print(self.income, self.age, self.rooms)
        
        # Reshape input values and make a prediction using the loaded model
        predicted = self.loaded_model.predict(np.array([self.income, self.age, self.rooms, self.baths, self.population]).reshape(1, -1))
        
        # Returning a dictionary with the predicted price
        return {'Predicted Price': predicted[0]}

# Creating an instance of the 'Controller' class
controller = Controller()
