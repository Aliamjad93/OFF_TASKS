from fastapi import FastAPI
from Controller.Controller import controller
from Model.Model import Model 
class Router:
    app=FastAPI()
    
    @app.get('/')
    def index():
        return "Welcome to Text Nature Level Prediction"
    
    
    @app.post('/')
    def prediction(text: Model):
        return controller.MakePrediction(text.text)


router=Router()        