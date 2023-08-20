# import necassary modules
from fastapi import FastAPI
from Controller.Controller import controller
from Model import Model

class Routes:
    # Define FastAPI routes using this class
    
    app = FastAPI()  # Create an instance of FastAPI
    
    @app.get('/')
    def index():
        # This function handles GET requests to the root URL ('/')
        return "Welcome to CHAT-GPT"  # Return a welcome message
    
    @app.post('/chatwithme')
    def ChatWithMe(text: Model.Model):
        # This function handles POST requests to '/chatwithme'
        # It expects input data with the structure defined by the Model.Model class
        
        # Call the AskQuestion method of the controller instance
        # Pass the user's input text from the input data
        return controller.AskQuestion(text.text)
    
# Create an instance of the Routes class to initialize the routes
route = Routes()
