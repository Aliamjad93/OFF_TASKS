# Importing necessary libraries
from .routes.router import Routes  # Importing the 'Routes' class from 'routes.temp' module
import uvicorn  # Importing uvicorn for running the FastAPI app

# Defining a function called 'start'
def start():
    # Running the FastAPI app using uvicorn
    # "app.main:Routes.App" specifies the app location and its attribute to run
    uvicorn.run("app.main:Routes.App", host="127.0.0.1", port=8000)
