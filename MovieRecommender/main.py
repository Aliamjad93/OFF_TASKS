# Import the 'router' instance from the Router module
from Router.router import router

# Import the 'uvicorn' library for running the FastAPI app
import uvicorn

# Entry point of the script
if __name__ == "__main__":
    # Run the FastAPI app using uvicorn

    # Specify the FastAPI app instance (router.app) to run
    # Bind the app to the localhost (127.0.0.1) on port 8000
    uvicorn.run(router.app, host="127.0.0.1", port=8000)
