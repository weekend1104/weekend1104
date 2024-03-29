from typing import Union,List
from pydantic import BaseModel,Field

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


#组合嵌套使用，方便多个内容提交
class MultipleItem(BaseModel):
    Items:List[Item]