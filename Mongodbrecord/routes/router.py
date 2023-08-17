from fastapi import FastAPI
from model.models import Student  # Import the Student model
from controller.controller import Controller  # Import the Controller class

class Routess:
    app = FastAPI()
    controller = Controller()  # Create a single instance of the Controller class
    
    @app.get('/')
    def Index():
        return Controller.Main()  # Call the Main method from the Controller
    
    @app.get('/getAll')
    def GetData():
        return Controller.Get_Data()  # Call the Get_Data method from the Controller
    
    @app.post('/create')
    def Add_data(data: Student):
        return Controller.Create_Data(data)  # Call the Create_Data method from the Controller
    
    @app.get('/getspec/{id}')
    def Get_Specific_Data(id: str):
        return Controller.Get_Specific_Data(id)  # Call the Get_Specific_Data method from the Controller

Routes = Routess()  # Create an instance of the Routess class
