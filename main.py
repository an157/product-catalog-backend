
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Product Catalog Backend"}


@app.get("/products")
def get_products():
    return [
        {
            "id": 1,
            "name": "Laptop",
            "price": 999.99
        },
        {
            "id": 2,
            "name": "Mouse",
            "price": 49.99
        }
    ]
