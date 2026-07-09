from fastapi import APIRouter
from app.database import cursor


router = APIRouter(
    prefix="/details",
    tags=["Product Details"]
)


@router.get("/products")
def product_details():

    cursor.execute("""
        SELECT
            p.product_id,
            p.name,
            p.price,
            c.category_name,
            s.subcategory_name

        FROM products p

        JOIN categories c
        ON p.category_id=c.category_id

        JOIN sub_categories s
        ON p.subcategory_id=s.subcategory_id

    """)


    rows = cursor.fetchall()


    result=[]


    for row in rows:

        result.append({

            "product_id":row[0],
            "name":row[1],
            "price":row[2],
            "category":row[3],
            "subcategory":row[4]

        })


    return result