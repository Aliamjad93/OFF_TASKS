from fastapi import FastAPI
from model.Model import Model
from Controller.controller import Controller
class route:
    app=FastAPI()
    

    # All Data Route    
    @app.get('/alldata')
    def AllData():
        return Controller.Alldata()
        
    # Prediction Route
    @app.post('/predict')
    def predict(name:Model):
        
        return Controller.Predict(name.movie_name)
        
    
    
    
router=route()

