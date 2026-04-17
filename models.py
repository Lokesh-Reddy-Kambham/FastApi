from pydantic import BaseModel
class Product(BaseModel):
    id:int
    name:str
    description:str
    price:float
    quantity:int
    # when we using BaseModel from Pydantic , then no need to use constructor
    # it's automatically create a constructor
    # def __int__(self,id,name,description,price,quantity):
    #     self.id = id
    #     self.name = name
    #     self.description = description
    #     self.price = price
    #     self.quantity =  quantity