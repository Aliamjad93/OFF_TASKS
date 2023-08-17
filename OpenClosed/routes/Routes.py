# Import necessary modules from FastAPI
from fastapi import FastAPI, UploadFile, File

# Import the controller instance from the Controller module
from controller.Controller import obj_controller

# Class defining the routes for FastAPI
class Routes:
    # Initialize the FastAPI app
    app = FastAPI()
    
    # Route for the root endpoint
    @app.get('/')
    def index():
        # Return a welcome message
        return {'message': 'Welcome to Cat vs Dog Prediction'}
    
    # Route for image prediction
    @app.post('/predicts')
    def AddImage(file: UploadFile = File(...)):
        # Call the prediction method from the controller and return the result
        return obj_controller.predict(file)

# Create an instance of the Routes class to define the routes
route = Routes()
