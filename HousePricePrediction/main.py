from Route import routes

from dotenv import load_dotenv
import os
import uvicorn



if __name__=='__main__':
    
    
    load_dotenv(dotenv_path="C:/Users/farha/.spyder-py3/Task1/HousePricePrediction/NewTextDocument.env")
    port=os.getenv("port")
    
    uvicorn.run(routes.Rout.app,host="127.0.0.1",port=port)