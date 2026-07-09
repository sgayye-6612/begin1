from app.database import conn, cursor

#PRODUCT CRUD OPERATIONS
def get_all_products():

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

    products=[]

    for row in rows:

        products.append({

            "product_id": row[0],
            "name": row[1],
            "price": row[2],
            "category_id": row[3],
            "subcategory_id": row[4]

        })

    return products



def get_product(product_id):

    cursor.execute("""
        SELECT
            product_id,
            name,
            price,
            category_id,
            subcategory_id
        FROM products
        WHERE product_id=%s
    """,(product_id,))


    return cursor.fetchone()



def create_product(product):

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

    return product

#CUSTOMER CRUD OPERATIONS
def get_all_customers():

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



def get_customer(customer_id):

    cursor.execute("""
        SELECT
            customer_id,
            name,
            email,
            phone,
            address
        FROM customer_details
        WHERE customer_id=%s
    """,
    (customer_id,))

    return cursor.fetchone()



def create_customer(customer):

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

    return customer

# =========================
# ORDER CRUD
# =========================


def get_all_orders():

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



def get_order(order_id):

    cursor.execute("""
        SELECT
            order_id,
            customer_id,
            product_id,
            quantity,
            order_date
        FROM order_details
        WHERE order_id=%s
    """,
    (order_id,))


    return cursor.fetchone()



def create_order(order):

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


    return order

# =========================
# CATEGORY CRUD
# =========================


def get_all_categories():

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



def get_category(category_id):

    cursor.execute("""
        SELECT
            category_id,
            category_name
        FROM categories
        WHERE category_id=%s
    """,
    (category_id,))


    return cursor.fetchone()



def create_category(category):

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


    return category

# =========================
# SUBCATEGORY CRUD
# =========================


def get_all_subcategories():

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



def get_subcategory(subcategory_id):

    cursor.execute("""
        SELECT
            subcategory_id,
            subcategory_name,
            category_id
        FROM sub_categories
        WHERE subcategory_id=%s
    """,
    (subcategory_id,))


    return cursor.fetchone()



def create_subcategory(subcategory):

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


    return subcategory

# =========================
# UPDATE PRODUCT
# =========================


def update_product(product_id, product):

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


    return cursor.rowcount



# =========================
# DELETE PRODUCT
# =========================


def delete_product(product_id):

    cursor.execute("""
        DELETE FROM products
        WHERE product_id=%s
    """,
    (product_id,))


    conn.commit()


    return cursor.rowcount

# =========================
# UPDATE CUSTOMER
# =========================


def update_customer(customer_id, customer):

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


    return cursor.rowcount



# =========================
# DELETE CUSTOMER
# =========================


def delete_customer(customer_id):

    cursor.execute("""
        DELETE FROM customer_details
        WHERE customer_id=%s
    """,
    (customer_id,))


    conn.commit()


    return cursor.rowcount

# =========================
# UPDATE ORDER
# =========================


def update_order(order_id, order):

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


    return cursor.rowcount



# =========================
# DELETE ORDER
# =========================


def delete_order(order_id):

    cursor.execute("""
        DELETE FROM order_details
        WHERE order_id=%s
    """,
    (order_id,))


    conn.commit()


    return cursor.rowcount


# UPDATE CATEGORY

def update_category(category_id, category):

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

    return cursor.rowcount



# DELETE CATEGORY

def delete_category(category_id):

    cursor.execute("""
        DELETE FROM categories
        WHERE category_id=%s
    """,
    (category_id,))

    conn.commit()

    return cursor.rowcount

# UPDATE SUBCATEGORY

def update_subcategory(subcategory_id, subcategory):

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

    return cursor.rowcount



# DELETE SUBCATEGORY

def delete_subcategory(subcategory_id):

    cursor.execute("""
        DELETE FROM sub_categories
        WHERE subcategory_id=%s
    """,
    (subcategory_id,))

    conn.commit()

    return cursor.rowcount