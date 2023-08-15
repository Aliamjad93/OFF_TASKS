    
from fastapi import FastAPI
# from model.models import Student
from app.model.models import Student
from app.controller.controller import Controller

class Routess:
    App = FastAPI()
    controller = Controller()  # Create a single instance of the Controller class
    
    @App.get('/')
    def Index():
        return Controller.Main()
    
    @App.get('/getAll')
    def Get_Data():
        return Controller.Data()
    
    @App.post('/create')
    def Add_data(data: Student):
        return Controller.Create_Data(data)
    
    @App.get('/getspec/{id}')
    def Get_Specific_Data(id: str):
        return Controller.Get_Specific_Data(id)

Routes = Routess()
  
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
