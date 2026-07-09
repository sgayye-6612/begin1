from fastapi import FastAPI

from app.routers import products, customers, orders ,categories, subcategories

from app.routers import details

app = FastAPI()


@app.get("/")
def home():

    return {
        "message":"Welcome to Ecommerce API!"
    }



app.include_router(products.router)

app.include_router(customers.router)

app.include_router(orders.router)

app.include_router(categories.router)

app.include_router(subcategories.router)

app.include_router(details.router)