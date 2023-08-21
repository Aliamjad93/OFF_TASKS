from Router.Router import router
import uvicorn
from dotenv import load_dotenv
import os

if __name__=="__main__":
    load_dotenv(dotenv_path=r"C:\Users\farha\.spyder-py3\Task1\SentimentAnalysis\Controller\src.env")
    port=os.get("port")
    host=os.get("host")
    uvicorn.run(router.app,host=host,port=port)