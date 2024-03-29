from pydantic import BaseModel

class LoginUser(BaseModel):
    name:str
    password:str
    