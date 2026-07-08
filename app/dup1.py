from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from database import conn, cursor

app = FastAPI()


# =====================================================
# MODELS
# =====================================================

class Product(BaseModel):
    product_id: int
    name: str
    price: float
    category_id: int
    subcategory_id: int


class Customer(BaseModel):
    customer_id: int
    name: str
    email: str
    phone: str
    address: str


class Order(BaseModel):
    customer_id: int
    product_id: int
    quantity: int
    order_date: str


class Category(BaseModel):
    category_id: int
    category_name: str


class SubCategory(BaseModel):
    subcategory_id: int
    subcategory_name: str
    category_id: int


class Support(BaseModel):
    name: str
    email: str
    message: str


# =====================================================
# HOME
# =====================================================

@app.get("/")
def home():
    return {
        "message": "Welcome to Ecommerce API!"
    }


# =====================================================
# PRODUCT APIs
# =====================================================

# GET ALL PRODUCTS

@app.get("/products")
def get_products():

    cursor.execute("""
        SELECT
            product_id,
            name,
            price,
            category_id,
            subcategory_id
        FROM products
    """)

    rows = cursor.fetchall()

    products = []

    for row in rows:

        products.append({

            "product_id": row[0],
            "name": row[1],
            "price": row[2],
            "category_id": row[3],
            "subcategory_id": row[4]

        })

    return products


# GET SINGLE PRODUCT

@app.get("/products/{product_id}")
def get_product(product_id: int):

    cursor.execute("""
        SELECT
            product_id,
            name,
            price,
            category_id,
            subcategory_id
        FROM products
        WHERE product_id=%s
    """, (product_id,))

    product = cursor.fetchone()

    if product is None:

        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return {

        "product_id": product[0],
        "name": product[1],
        "price": product[2],
        "category_id": product[3],
        "subcategory_id": product[4]

    }


# ADD PRODUCT

@app.post("/products")
def add_product(product: Product):

    cursor.execute("""
        INSERT INTO products
        (
            product_id,
            name,
            price,
            category_id,
            subcategory_id
        )

        VALUES(%s,%s,%s,%s,%s)
    """,

    (

        product.product_id,
        product.name,
        product.price,
        product.category_id,
        product.subcategory_id

    ))

    conn.commit()

    return {

        "message": "Product added successfully",
        "product": product

    }


# UPDATE PRODUCT

@app.put("/products/{product_id}")
def update_product(product_id: int, product: Product):

    cursor.execute("""

        UPDATE products

        SET
            name=%s,
            price=%s,
            category_id=%s,
            subcategory_id=%s

        WHERE product_id=%s

    """,

    (

        product.name,
        product.price,
        product.category_id,
        product.subcategory_id,
        product_id

    ))

    conn.commit()

    if cursor.rowcount == 0:

        raise HTTPException(

            status_code=404,
            detail="Product not found"

        )

    return {

        "message": "Product updated successfully"

    }


# DELETE PRODUCT

@app.delete("/products/{product_id}")
def delete_product(product_id: int):

    cursor.execute("""

        DELETE FROM products

        WHERE product_id=%s

    """,

    (product_id,))

    conn.commit()

    if cursor.rowcount == 0:

        raise HTTPException(

            status_code=404,
            detail="Product not found"

        )

    return {

        "message": "Product deleted successfully"

    }

# =====================================================
# CUSTOMER APIs
# =====================================================

# GET ALL CUSTOMERS

@app.get("/customers")
def get_customers():

    cursor.execute("""
        SELECT
            customer_id,
            name,
            email,
            phone,
            address
        FROM customer_details
    """)

    rows = cursor.fetchall()

    customers = []

    for row in rows:

        customers.append({

            "customer_id": row[0],
            "name": row[1],
            "email": row[2],
            "phone": row[3],
            "address": row[4]

        })

    return customers


# GET SINGLE CUSTOMER

@app.get("/customers/{customer_id}")
def get_customer(customer_id: int):

    cursor.execute("""
        SELECT
            customer_id,
            name,
            email,
            phone,
            address
        FROM customer_details
        WHERE customer_id=%s
    """, (customer_id,))

    customer = cursor.fetchone()

    if customer is None:

        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    return {

        "customer_id": customer[0],
        "name": customer[1],
        "email": customer[2],
        "phone": customer[3],
        "address": customer[4]

    }


# ADD CUSTOMER

@app.post("/customers")
def add_customer(customer: Customer):

    cursor.execute("""
        INSERT INTO customer_details
        (
            customer_id,
            name,
            email,
            phone,
            address
        )

        VALUES(%s,%s,%s,%s,%s)
    """,

    (

        customer.customer_id,
        customer.name,
        customer.email,
        customer.phone,
        customer.address

    ))

    conn.commit()

    return {

        "message": "Customer added successfully",
        "customer": customer

    }


# UPDATE CUSTOMER

@app.put("/customers/{customer_id}")
def update_customer(customer_id: int, customer: Customer):

    cursor.execute("""
        UPDATE customer_details

        SET
            name=%s,
            email=%s,
            phone=%s,
            address=%s

        WHERE customer_id=%s
    """,

    (

        customer.name,
        customer.email,
        customer.phone,
        customer.address,
        customer_id

    ))

    conn.commit()

    if cursor.rowcount == 0:

        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    return {

        "message": "Customer updated successfully"

    }


# DELETE CUSTOMER

@app.delete("/customers/{customer_id}")
def delete_customer(customer_id: int):

    cursor.execute("""
        DELETE FROM customer_details
        WHERE customer_id=%s
    """,

    (customer_id,))

    conn.commit()

    if cursor.rowcount == 0:

        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    return {

        "message": "Customer deleted successfully"

    }

# =====================================================
# ORDER APIs
# =====================================================

# GET ALL ORDERS

@app.get("/orders")
def get_orders():

    cursor.execute("""
        SELECT
            order_id,
            customer_id,
            product_id,
            quantity,
            order_date
        FROM order_details
    """)

    rows = cursor.fetchall()

    orders = []

    for row in rows:

        orders.append({

            "order_id": row[0],
            "customer_id": row[1],
            "product_id": row[2],
            "quantity": row[3],
            "order_date": row[4]

        })

    return orders


# GET SINGLE ORDER

@app.get("/orders/{order_id}")
def get_order(order_id: int):

    cursor.execute("""
        SELECT
            order_id,
            customer_id,
            product_id,
            quantity,
            order_date
        FROM order_details
        WHERE order_id=%s
    """, (order_id,))

    order = cursor.fetchone()

    if order is None:

        raise HTTPException(
            status_code=404,
            detail="Order not found"
        )

    return {

        "order_id": order[0],
        "customer_id": order[1],
        "product_id": order[2],
        "quantity": order[3],
        "order_date": order[4]

    }


# ADD ORDER

@app.post("/orders")
def add_order(order: Order):

    cursor.execute("""
        INSERT INTO order_details
        (
            customer_id,
            product_id,
            quantity,
            order_date
        )

        VALUES(%s,%s,%s,%s)
    """,

    (

        order.customer_id,
        order.product_id,
        order.quantity,
        order.order_date

    ))

    conn.commit()

    return {

        "message": "Order added successfully",
        "order": order

    }


# UPDATE ORDER

@app.put("/orders/{order_id}")
def update_order(order_id: int, order: Order):

    cursor.execute("""
        UPDATE order_details

        SET
            customer_id=%s,
            product_id=%s,
            quantity=%s,
            order_date=%s

        WHERE order_id=%s
    """,

    (

        order.customer_id,
        order.product_id,
        order.quantity,
        order.order_date,
        order_id

    ))

    conn.commit()

    if cursor.rowcount == 0:

        raise HTTPException(
            status_code=404,
            detail="Order not found"
        )

    return {

        "message": "Order updated successfully"

    }


# DELETE ORDER

@app.delete("/orders/{order_id}")
def delete_order(order_id: int):

    cursor.execute("""
        DELETE FROM order_details
        WHERE order_id=%s
    """, (order_id,))

    conn.commit()

    if cursor.rowcount == 0:

        raise HTTPException(
            status_code=404,
            detail="Order not found"
        )

    return {

        "message": "Order deleted successfully"

    }


# =====================================================
# CATEGORY APIs
# =====================================================

# GET ALL CATEGORIES

@app.get("/categories")
def get_categories():

    cursor.execute("""
        SELECT
            category_id,
            category_name
        FROM categories
    """)

    rows = cursor.fetchall()

    categories = []

    for row in rows:

        categories.append({

            "category_id": row[0],
            "category_name": row[1]

        })

    return categories


# GET SINGLE CATEGORY

@app.get("/categories/{category_id}")
def get_category(category_id: int):

    cursor.execute("""
        SELECT
            category_id,
            category_name
        FROM categories
        WHERE category_id=%s
    """, (category_id,))

    category = cursor.fetchone()

    if category is None:

        raise HTTPException(
            status_code=404,
            detail="Category not found"
        )

    return {

        "category_id": category[0],
        "category_name": category[1]

    }


# ADD CATEGORY

@app.post("/categories")
def add_category(category: Category):

    cursor.execute("""
        INSERT INTO categories
        (
            category_id,
            category_name
        )

        VALUES(%s,%s)
    """,

    (

        category.category_id,
        category.category_name

    ))

    conn.commit()

    return {

        "message": "Category added successfully",
        "category": category

    }
# =====================================================
# UPDATE CATEGORY
# =====================================================

@app.put("/categories/{category_id}")
def update_category(category_id: int, category: Category):

    cursor.execute("""
        UPDATE categories
        SET category_name=%s
        WHERE category_id=%s
    """,
    (
        category.category_name,
        category_id
    ))

    conn.commit()

    if cursor.rowcount == 0:
        raise HTTPException(
            status_code=404,
            detail="Category not found"
        )

    return {
        "message": "Category updated successfully"
    }


# =====================================================
# DELETE CATEGORY
# =====================================================

@app.delete("/categories/{category_id}")
def delete_category(category_id: int):

    cursor.execute("""
        DELETE FROM categories
        WHERE category_id=%s
    """,
    (category_id,))

    conn.commit()

    if cursor.rowcount == 0:
        raise HTTPException(
            status_code=404,
            detail="Category not found"
        )

    return {
        "message": "Category deleted successfully"
    }


# =====================================================
# SUBCATEGORY APIs
# =====================================================

# GET ALL SUBCATEGORIES

@app.get("/subcategories")
def get_subcategories():

    cursor.execute("""
        SELECT
            subcategory_id,
            subcategory_name,
            category_id
        FROM sub_categories
    """)

    rows = cursor.fetchall()

    subcategories = []

    for row in rows:

        subcategories.append({

            "subcategory_id": row[0],
            "subcategory_name": row[1],
            "category_id": row[2]

        })

    return subcategories


# GET SINGLE SUBCATEGORY

@app.get("/subcategories/{subcategory_id}")
def get_subcategory(subcategory_id: int):

    cursor.execute("""
        SELECT
            subcategory_id,
            subcategory_name,
            category_id
        FROM sub_categories
        WHERE subcategory_id=%s
    """,
    (subcategory_id,))

    subcategory = cursor.fetchone()

    if subcategory is None:

        raise HTTPException(
            status_code=404,
            detail="Subcategory not found"
        )

    return {

        "subcategory_id": subcategory[0],
        "subcategory_name": subcategory[1],
        "category_id": subcategory[2]

    }


# ADD SUBCATEGORY

@app.post("/subcategories")
def add_subcategory(subcategory: SubCategory):

    cursor.execute("""
        INSERT INTO sub_categories
        (
            subcategory_id,
            subcategory_name,
            category_id
        )

        VALUES(%s,%s,%s)
    """,
    (
        subcategory.subcategory_id,
        subcategory.subcategory_name,
        subcategory.category_id
    ))

    conn.commit()

    return {
        "message": "Subcategory added successfully",
        "subcategory": subcategory
    }


# UPDATE SUBCATEGORY

@app.put("/subcategories/{subcategory_id}")
def update_subcategory(subcategory_id: int, subcategory: SubCategory):

    cursor.execute("""
        UPDATE sub_categories

        SET
            subcategory_name=%s,
            category_id=%s

        WHERE subcategory_id=%s
    """,
    (
        subcategory.subcategory_name,
        subcategory.category_id,
        subcategory_id
    ))

    conn.commit()

    if cursor.rowcount == 0:

        raise HTTPException(
            status_code=404,
            detail="Subcategory not found"
        )

    return {
        "message": "Subcategory updated successfully"
    }


# DELETE SUBCATEGORY

@app.delete("/subcategories/{subcategory_id}")
def delete_subcategory(subcategory_id: int):

    cursor.execute("""
        DELETE FROM sub_categories
        WHERE subcategory_id=%s
    """,
    (subcategory_id,))

    conn.commit()

    if cursor.rowcount == 0:

        raise HTTPException(
            status_code=404,
            detail="Subcategory not found"
        )

    return {
        "message": "Subcategory deleted successfully"
    }


# =====================================================
# PRODUCT DETAILS (JOIN)
# =====================================================

@app.get("/products/details")
def get_product_details():

    cursor.execute("""
        SELECT

            p.product_id,
            p.name,
            p.price,

            c.category_name,

            s.subcategory_name

        FROM products p

        JOIN categories c
        ON p.category_id = c.category_id

        JOIN sub_categories s
        ON p.subcategory_id = s.subcategory_id

        ORDER BY p.product_id
    """)

    rows = cursor.fetchall()

    products = []

    for row in rows:

        products.append({

            "product_id": row[0],
            "product_name": row[1],
            "price": row[2],
            "category": row[3],
            "subcategory": row[4]

        })

    return products