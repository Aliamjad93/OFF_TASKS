
#------ FastAPI Modules

from fastapi import FastAPI, UploadFile, File

from controller.Controller import obj_contoller




class Routes:
    app=FastAPI()
    
    
    
    @app.get('/')
    def index():
        return {'message': 'Welcome to Cat vs Dog Prediction'}
    
    @app.post('/predicts')
    def AddImage(file: UploadFile= File(...)):
        
        return obj_contoller.predict(file)
        


        
    

route=Routes()
    


