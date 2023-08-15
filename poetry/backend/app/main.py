# from routes import temp
from .routes.temp import Routes    
import uvicorn



def start():
    
    uvicorn.run("app.main:Routes.App" ,host="127.0.0.1",port=8000)