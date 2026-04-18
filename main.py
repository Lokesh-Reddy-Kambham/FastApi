from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from models import Product
from database import session , engine
import database_model 

app = FastAPI()

database_model.Base.metadata.create_all(bind=engine)

@app.get("/")
def greet():
    return "Welcome to My World"

products = [
    Product(id=1, name="Redmi", description="Budget-Friendly product", price=13555.57, quantity=2),
    Product(id=2, name="IQOO", description="Best Product at this price", price=13555.57, quantity=3),
    Product(id=3, name="Samsung", description="Camera oriented product", price=13555.57, quantity=4),
    Product(id=4, name="OnePlus", description="Good UI Product", price=13555.57, quantity=5)
]

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()
 
def init_db():
    db = session()

    count = db.query(database_model.Product).count()

    if count == 0:
        for product in products:
            db.add(database_model.Product(**product.model_dump()))
        db.commit()

init_db()

@app.get("/products")
def get_all_products(db: Session = Depends(get_db)): 
    db_products = db.query(database_model.Product).all()
    return db_products

@app.get("/product/{id}")
def get_product_by_id(id:int,db: Session = Depends(get_db)):
    db_product = db.query(database_model.Product).filter(database_model.Product.id == id).first()
    if db_product:
            return db_product
    return "Product is not Listed"


@app.post("/add_product")
def add_product(product: Product,db: Session = Depends(get_db)):
    db.add(database_model.Product(**product.model_dump()))
    db.commit()
    return product


@app.put("/update_product")
def update_product(id:int , product:Product,db: Session = Depends(get_db)):
    db_product = db.query(database_model.Product).filter(database_model.Product.id == id).first()
    if db_product:
        db_product.name = product.name # type: ignore
        db_product.description = product.description # type: ignore
        db_product.price = product.price # type: ignore
        db_product.quantity = product.quantity # type: ignore
        db.commit()
        return db_product
    else:
        return "product is not found"

@app.delete("/delete_products")    
def delete_product(id:int,db: Session = Depends(get_db)):
    db_product = db.query(database_model.Product).filter(database_model.Product.id == id).first()
    if db_product:
            db.delete(db_product)
            db.commit()
            return "Deleted Given product"
    else:
        return "product is not found"