from routes import temp

import uvicorn



if __name__=='__main__':
    uvicorn.run(temp.Routes.app,host="127.0.0.1",port=8000)