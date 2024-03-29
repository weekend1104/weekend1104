from fastapi import APIRouter,Form,Header
# from application.login.loginbasemodels import LoginUser
from starlette.responses import JSONResponse


applogin = APIRouter()


@applogin.post("/")
async def login(authorization: str = Header(None),
                content_type: str = Header(None)
                ):
    print(authorization)
    print(content_type)

    return JSONResponse({
        "Hello": "World",
        "lesson": "one",
        "per":101
         })

