from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.database import conn, cursor

app = FastAPI()

class Product(BaseModel):
    id: int
    name: str
    price: float


@app.get("/")
def home():
    return {"message": "Welcome to Ecommerce API!"}

# GET ALL PRODUCTS
@app.get("/products")
def get_products():

    cursor.execute("SELECT id, name, price FROM products")

    rows = cursor.fetchall()

    products = []

    for row in rows:
        products.append({
            "id": row[0],
            "name": row[1],
            "price": row[2]
        })

    return products

# GET SINGLE PRODUCT
@app.get("/products/{product_id}")
def get_product(product_id: int):

    cursor.execute(
        "SELECT id, name, price FROM products WHERE id=%s",
        (product_id,)
    )

    product = cursor.fetchone()

    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")

    return {
        "id": product[0],
        "name": product[1],
        "price": product[2]
    }

# ADD PRODUCT
@app.post("/products")
def add_product(product: Product):

    cursor.execute(
        "INSERT INTO products (id, name, price) VALUES (%s, %s, %s)",
        (product.id, product.name, product.price)
    )

    conn.commit()

    return {
        "message": "Product added successfully",
        "product": product
    }

# UPDATE PRODUCT
@app.put("/products/{product_id}")
def update_product(product_id: int, product: Product):

    cursor.execute(
        """
        UPDATE products
        SET name=%s,
            price=%s
        WHERE id=%s
        """,
        (product.name, product.price, product_id)
    )

    conn.commit()

    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Product not found")

    return {"message": "Product updated successfully"}

# DELETE PRODUCT
@app.delete("/products/{product_id}")
def delete_product(product_id: int):

    cursor.execute(
        "DELETE FROM products WHERE id=%s",
        (product_id,)
    )

    conn.commit()

    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Product not found")

    return {"message": "Product deleted successfully"}

