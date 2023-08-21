# Import the router instance from the Router module
from Router.Router import router

# Import uvicorn for running the FastAPI app
import uvicorn

# Import the load_dotenv function and os module
from dotenv import load_dotenv
import os

# Check if this script is being executed as the main program
if __name__ == "__main__":
    # Load environment variables from the specified file
    load_dotenv(dotenv_path=r"C:\Users\farha\.spyder-py3\Task1\SentimentAnalysis\Controller\src.env")
    
    # Get the port and host from environment variables
    port = (os.getenv("port"))  
    host = os.getenv("host")
    
    # Run the FastAPI app using uvicorn
    uvicorn.run(router.app, host=host, port=port)
