# Importing necessary libraries
from fastapi import FastAPI  # Required for creating the FastAPI app
from app.model.models import Student  # Importing the 'Student' model
from app.controller.controller import Controller  # Importing the 'Controller' class

# Creating a class called 'Routess'
class Routess:
    App = FastAPI()  # Creating an instance of 'FastAPI'
    controller = Controller()  # Create a single instance of the Controller class
    
    # Defining a route for the root URL '/'
    @App.get('/')
    def Index():
        return Controller.Main()  # Calling the 'Main' method from the 'Controller' instance
    
    # Defining a route for '/getAll' endpoint
    @App.get('/getAll')
    def GetData():
        return Controller.Get_Data()  # Calling the 'Data' method from the 'Controller' instance
    
    # Defining a route for '/create' endpoint using HTTP POST method
    @App.post('/create')
    def Add_data(data: Student):
        return Controller.Create_Data(data)  # Calling the 'Create_Data' method from the 'Controller' instance
    
    # Defining a route for '/getspec/{id}' endpoint with a path parameter 'id'
    @App.get('/getspec/{id}')
    def Get_Specific_Data(id: str):
        return Controller.Get_Specific_Data(id)  # Calling the 'Get_Specific_Data' method from the 'Controller' instance

# Creating an instance of the 'Routess' class
Routes = Routess()
