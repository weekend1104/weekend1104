from contextlib import asynccontextmanager
from fastapi import FastAPI,Header,status,Form,Request
from apprun import app
from application.pytoken import get_token
from starlette.responses import JSONResponse


# def fake_answer_to_everything_ml_model(x: float):
def fake_answer_to_everything_ml_model(Authorization: str):
    
    # return x * 42
    return Authorization

ml_models = {}

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the ML model
    ml_models["answer_to_everything"] = fake_answer_to_everything_ml_model
    yield
    # Clean up the ML models and release resources
    ml_models.clear()


@app.get("/CheckToken")
async def predict(Authorization = Header(None)):
    Authorization = Authorization.split()[1]
    result = ml_models["answer_to_everything"](Authorization)
    return {"result": result}


@app.get("/predict02")
async def predict():
    result = "dfadfafdafda"
    return {"result": result}


@app.post("/gettoken")
async def gettoken(request: Request,
                   username:str = Form(),
                   password:str = Form(),
                   ):
    token = get_token(username)
    print(f"username:{username},password:{password}")
    print(request.headers.get('Content-Type'))
    result = {"token":token}
    return JSONResponse(status_code=status.HTTP_200_OK,
                        content=result)