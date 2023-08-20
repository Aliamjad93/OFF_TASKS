from Routes import Routes
import uvicorn

if __name__=="__main__":
    uvicorn.run(Routes.route.app,host="127.0.0.1",port=8000)    
