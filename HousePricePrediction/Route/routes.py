# Importing the 'controller' instance from the 'Controller.controller' module
from Controller.controller import controller

# Importing the 'FastAPI' class from the 'fastapi' library
from fastapi import FastAPI

# Importing the 'House' model from the 'Model.Model' module
from Model.Model import House

# Creating a class called 'Routes'
class Routes:
    # Creating an instance of 'FastAPI'
    app = FastAPI()

    # Defining a route for the root URL '/'
    @app.get('/')
    def index():
        return {'message': 'Welcome to House Price Prediction'}

    # Defining a route for the '/predict' endpoint using HTTP POST method
    @app.post('/predict')
    def predict(data: House):
        # Using the 'controller' instance to make a prediction
        # and returning the predicted result
        return controller.MakePrediction(data.income, data.age, data.room, data.bath, data.population)

# Creating an instance of the 'Routes' class
Rout = Routes()
