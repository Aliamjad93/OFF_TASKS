
from routes.Routes import route
import uvicorn



if __name__=='__main__':
    uvicorn.run(route.app,host="127.0.0.1",port=8000)


    





























