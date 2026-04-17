from fastapi import FastAPI
from models import Product
app = FastAPI()

@app.get("/")
def greet():
    return "Welcome to My World"

products = [
    Product(id=1, name="Redmi", description="Budget-Friendly product", price=13555.57, quantity=2),
    Product(id=2, name="IQOO", description="Best Product at this price", price=13555.57, quantity=3),
    Product(id=3, name="Samsung", description="Camera oriented product", price=13555.57, quantity=4),
    Product(id=4, name="OnePlus", description="Good UI Product", price=13555.57, quantity=5)
]

@app.get("/products")
def get_all_products():
    return products

@app.get("/product/{id}")
def get_product_by_id(id:int):
    for product in products :
        if product.id == id:
            return product
    return "Product is not Listed"


@app.post("/add_product")
def add_product(product: Product):
    products.append(product)
    return product
@app.put("/update_product")
def update_product(id:int , product:Product):
    for i in range(len(products)):
        if products[i].id == id :
            products[i] = product
            return "Product Details Updated"
    else:
        return "product is not found"

@app.delete("/delete_products")    
def delete_product(id:int):
    for i in range(len(products)):
        if products[i].id == id :
            del products[i]
            return "Deleted Given product"
    else:
        return "product is not found"