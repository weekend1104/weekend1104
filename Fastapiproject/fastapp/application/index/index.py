from fastapi import APIRouter
from typing import Union,Optional
from application.index.basemodels import Item,MultipleItem
from starlette.responses import JSONResponse

indexs = APIRouter()

@indexs.get("/")
async def index1():
    return JSONResponse({
        "Hello": "World",
        "lesson": "one",
        "per":101
         })

 
@indexs.get("/items/{item_id}")
def read_item(item_id: int, 
              b: Union[str, None],    
              q: Union[str, None] = None, # 没有 = None 等于必选项
              price:Optional[int] = None # optional 等于union 缩写
    ):
    return {"item_id": item_id,"b": b, "q": q, "price":price}



@indexs.post("/items/addItem",tags=["单个商品提交"])
async def add_item(item:Item):

    return item

#多个商品提交 方式
@indexs.post("/items/addItems",tags=["多个商品提交"])
async def add_items(items:MultipleItem):
    
    return items



@indexs.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id, "item_price":item.price}
