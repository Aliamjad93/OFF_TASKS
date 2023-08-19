# Importing necessary libraries
from fastapi import FastAPI, File, UploadFile  # Required for creating FastAPI app and handling file uploads
from Model.model import lstm  # Importing the 'lstm' Pydantic model
from Controller.contoller import controller  # Importing the 'controller' instance

# Creating a class called 'Router'
class Router:
    # Creating an instance of 'FastAPI'
    app = FastAPI()

    # Defining a route for the root URL '/'
    @app.get('/')
    def index():
        return "Welcome to Next Word Predictor App"
    
    # Defining a route for the '/predict' endpoint using HTTP POST method
    @app.post('/predict')
    def Predict(inputName: lstm):  # Using the 'lstm' model to validate input data
        # Calling the 'MakePrediction' method from the 'controller' instance
        return controller.MakePrediction(inputName)

# Creating an instance of the 'Router' class
router = Router()
