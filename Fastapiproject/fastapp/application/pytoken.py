from fastapi import Header,status
from fastapi.responses import JSONResponse
from typing import Optional
from jwt import JWT,jwk_from_dict
from jwt.utils import b64encode,get_int_from_datetime
from datetime import datetime, timedelta, timezone
from jwt.exceptions import JWTDecodeError

signing_key = jwk_from_dict({'kty': 'oct',
                             'k': b64encode(b'''This is a bot shit applications!''')})

def get_token(uname) -> str:
    username = uname
    message = {'username':username,
            'iss': 'https://example.com/',
            'sub': 'yosida95',
            'iat': get_int_from_datetime(datetime.now(timezone.utc)),
            'exp': get_int_from_datetime(datetime.now(timezone.utc) + timedelta(hours=1))
        }

    encoded = JWT().encode(payload=message,key=signing_key,alg='HS256')

    return encoded

def decode_token(Authorization = Header(None)):
    if Authorization is None:
        return {
            "Verification":False,
            "message":"Token Is None."
        }
    else:
        Authorization = Authorization.split()[1]
        try:
            decode = JWT().decode(Authorization,key=signing_key)
            Verification = {
                "Verification":True,
                "message":"Verification passed."
            }
            return Verification
        except Exception as error:
            Verification = {
                "Verification":False,
                "message":repr(error)
            }
            return Verification



# if __name__ == "__main__":

#     maketoken = MakeTokens()
#     encodes = maketoken.get_token(uname="wanglaowu")
#     print(encodes)
#     print(type(encodes))
#     Tokendecode = maketoken.decode_token("encodes")
#     print(Tokendecode)
