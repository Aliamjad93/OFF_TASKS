from Routes import Routes
import uvicorn
# Importing the 'load_dotenv' function from the 'dotenv' library
from dotenv import load_dotenv

# Importing the 'os' module for working with environment variables
import os

if __name__=="__main__":
    # Load environment variables from .env file
    load_dotenv(dotenv_path="C:/Users/farha/.spyder-py3/Task1/ChatBot/src.env")
    
    # Access the 'port' environment variable
    host = os.getenv("host")
    port = os.getenv("port")
    uvicorn.run(Routes.route.app,host=host,port=port)    
