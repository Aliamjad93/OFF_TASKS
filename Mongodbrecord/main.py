from routes import router #importing router   
import uvicorn



if __name__=='__main__':
    uvicorn.run(router.Routes.app,host="127.0.0.1",port=8000) # calling my app