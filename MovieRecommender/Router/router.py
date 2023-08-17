# Import the FastAPI framework
from fastapi import FastAPI

# Import necessary classes from your project
from model.Model import Model
from Controller.controller import Controller

# Create a class for defining routes
class route:
    # Initialize the FastAPI app
    app = FastAPI()

    # Define a route for retrieving all data
    @app.get('/alldata')
    def AllData():
        # Call the Alldata() function from the Controller class to fetch all data
        return Controller.Alldata()

    # Define a route for making predictions
    @app.post('/predict')
    def predict(name: Model):
        # Extract the movie name from the input Model instance
        movie_name = name.movie_name
        # Call the Predict() function from the Controller class to make predictions
        return Controller.Predict(movie_name)

# Create an instance of the 'route' class to initialize routes
router = route()
