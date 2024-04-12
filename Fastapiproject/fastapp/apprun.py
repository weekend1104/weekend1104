import uvicorn
from fastapi import FastAPI
from application.index.index import indexs
from application.login.main import applogin
from application import projects


app = FastAPI(debug=True)

app.include_router(indexs,prefix='/indexs',tags=["索引"])
app.include_router(applogin,prefix='/login',tags=["登录"])

if __name__ == "__main__":
    uvicorn.run("apprun:app",host="127.0.0.1",port=9099,reload=True)