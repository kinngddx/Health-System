# from fastapi import FastAPI

# yeh schema create kiya hai ki request and response kis form me hoga 
from pydantic import BaseModel,ConfigDict

class ProductCreate(BaseModel):
    
    name: str 
    price: int
    stock: int  

    


class ProductResponse(BaseModel):
    id:int
    name: str 
    price: int
    stock: int
    #By setting from_attributes=True, you tell Pydantic: "If you don't find a dictionary key, look for an object attribute with that name instead."
    model_config=ConfigDict(from_attributes=True)




