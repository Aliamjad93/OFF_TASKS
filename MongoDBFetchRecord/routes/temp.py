    
from fastapi import FastAPI
from model.models import Student
from controller.controller import Controller

class Routess:
    app = FastAPI()
    controller = Controller()  # Create a single instance of the Controller class
    
    @app.get('/')
    def Index():
        return Controller.Main()
    
    @app.get('/getAll')
    def Get_Data():
        return Controller.Data()
    
    @app.post('/create')
    def Add_data(data: Student):
        return Controller.Create_Data(data)
    
    @app.get('/getspec/{id}')
    def Get_Specific_Data(id: str):
        return Controller.Get_Specific_Data(id)

Routes = Routess()
  
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
