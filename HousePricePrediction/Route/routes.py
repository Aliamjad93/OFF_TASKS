







from Controller.controller import controller
from fastapi import FastAPI
from Model.Model import House


class Routes:
    
    app=FastAPI()
    
    @app.get('/')
    def index():
        return {'message': 'Welcome to House Price Prediction'}
    
    @app.post('/predict')
    def predict(data:House):
        
        return controller.MakePrediction(data.income,data.age,data.room,data.bath,data.population)
    
Rout=Routes()
    
    
    
    
    
    
