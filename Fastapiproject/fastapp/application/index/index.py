from fastapi import APIRouter,Depends,status,UploadFile
from typing import Union,Optional,List
from application.index.basemodels import Item,MultipleItem
from starlette.responses import JSONResponse
from application.pytoken import decode_token

indexs = APIRouter()

@indexs.get("/")
async def index1(verify = Depends(decode_token)):

    if verify["Verification"]:
        return JSONResponse({
            "Hello": "World",
            "lesson": "one",
            "per":101
        })
    else:
        return JSONResponse(status_code=status.HTTP_501_NOT_IMPLEMENTED,content=verify)

 
@indexs.get("/items/{item_id}")
def read_item(item_id: int, 
              b: Union[str, None],    
              q: Union[str, None] = None, # 没有 = None 等于必选项
              price:Optional[int] = None, # optional 等于union 缩写
              verify = Depends(decode_token)
    ):
    if verify["Verification"]:
        return JSONResponse(content={"item_id": item_id,"b": b, "q": q, "price":price})
    else:
        return JSONResponse(status_code=status.HTTP_501_NOT_IMPLEMENTED,content=verify)



@indexs.post("/items/addItem",tags=["单个商品提交"])
async def add_item(item:Item,
                   verify = Depends(decode_token)):

    return item

#多个商品提交 方式
@indexs.post("/items/addItems",tags=["多个商品提交"])
async def add_items(items:MultipleItem):
    
    return items



@indexs.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id, "item_price":item.price}


#获取uploadfile，file作为获取post form-data的对象
@indexs.post("/uploadfile")
def uploadfile(file: UploadFile):
    names = file.filename.split('.')
    return {"uploadfilename":file.filename,
            "filename":names[0],
            "filepath":names[1]
            }

#获取列表的uploadfile
@indexs.post("/uploadfiles")
def uploadfiles(files: List[UploadFile]):
    return {"uploadfilescounts":files.count()}