# Importing the 'routes' instance from the 'Route' module
from Route import routes

# Importing the 'load_dotenv' function from the 'dotenv' library
from dotenv import load_dotenv

# Importing the 'os' module for working with environment variables
import os

# Importing the 'uvicorn' library to run the FastAPI app
import uvicorn

# Check if the script is being run as the main program
if __name__ == '__main__':
    # Load environment variables from .env file
    load_dotenv(dotenv_path="C:/Users/farha/.spyder-py3/Task1/HousePricePrediction/NewTextDocument.env")
    
    # Access the 'port' environment variable
    port = os.getenv("port")
    
    # Run the FastAPI app using the 'uvicorn' library
    uvicorn.run(routes.Rout.app, host="127.0.0.1", port=port)
