from fastapi import FastAPI
from Controller.Controller import controller
from Model.Model import Model 

# Create an instance of FastAPI
class Router:
    app = FastAPI()

    # Define a route for the root URL
    @app.get('/')
    def index():
        return "Welcome to Text Nature Level Prediction"

    # Define a route for handling POST requests
    @app.post('/')
    def prediction(text: Model):
        # Call the MakePrediction method from the controller
        return controller.MakePrediction(text.text)

# Create an instance of the Router class
router = Router()
