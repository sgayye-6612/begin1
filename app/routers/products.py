from fastapi import APIRouter, HTTPException

from app import crud
from app.schemas import Product


router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


# GET ALL PRODUCTS

@router.get("/")
def get_products():

    return crud.get_all_products()



# GET SINGLE PRODUCT

@router.get("/{product_id}")
def get_product(product_id:int):

    product = crud.get_product(product_id)


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

@router.post("/")
def add_product(product:Product):

    result = crud.create_product(product)


    return {

        "message":"Product added successfully",
        "product":result

    }

# UPDATE PRODUCT

@router.put("/{product_id}")
def update_product(product_id:int, product:Product):

    result = crud.update_product(product_id, product)


    if result == 0:

        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )


    return {
        "message":"Product updated successfully"
    }



# DELETE PRODUCT

@router.delete("/{product_id}")
def delete_product(product_id:int):

    result = crud.delete_product(product_id)


    if result == 0:

        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )


    return {
        "message":"Product deleted successfully"
    }