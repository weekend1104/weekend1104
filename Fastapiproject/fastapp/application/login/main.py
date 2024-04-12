from fastapi import APIRouter
import base64
# from application.login.loginbasemodels import LoginUser
from starlette.responses import JSONResponse
from application.pytoken import get_token


applogin = APIRouter()


