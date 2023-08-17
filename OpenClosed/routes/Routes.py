# Importing necessary libraries
from fastapi import FastAPI, UploadFile, File  # Importing FastAPI, UploadFile, and File classes
from controller.Controller import obj_controller  # Importing the 'obj_controller' instance from the 'Controller' module

# Creating a class called 'Routes'
class Routes:
    app = FastAPI()  # Creating an instance of 'FastAPI'
    
    # Defining a route for the root URL '/'
    @app.get('/')
    def index():
        return {'message': 'Welcome to Cat vs Dog Prediction'}
    
    # Defining a route for '/predicts' endpoint using HTTP POST method
    @app.post('/predicts')
    def AddImage(file: UploadFile = File(...)):  # Using 'UploadFile' to handle uploaded image
        return obj_controller.predict(file)  # Calling the 'predict' method from the 'obj_controller' instance

# Creating an instance of the 'Routes' class
route = Routes()
