from fastapi import APIRouter, HTTPException

from app import crud
from app.schemas import Category



router = APIRouter(
    prefix="/categories",
    tags=["Categories"]
)



# GET ALL CATEGORIES

@router.get("/")
def get_categories():

    return crud.get_all_categories()



# GET SINGLE CATEGORY

@router.get("/{category_id}")
def get_category(category_id:int):

    category = crud.get_category(category_id)


    if category is None:

        raise HTTPException(
            status_code=404,
            detail="Category not found"
        )


    return {

        "category_id": category[0],
        "category_name": category[1]

    }



# CREATE CATEGORY

@router.post("/")
def add_category(category:Category):

    result = crud.create_category(category)


    return {

        "message":"Category added successfully",
        "category":result

    }


@router.put("/{category_id}")
def update_category(category_id:int, category:Category):

    result = crud.update_category(category_id, category)

    if result == 0:
        raise HTTPException(
            status_code=404,
            detail="Category not found"
        )

    return {
        "message":"Category updated successfully"
    }



@router.delete("/{category_id}")
def delete_category(category_id:int):

    result = crud.delete_category(category_id)

    if result == 0:
        raise HTTPException(
            status_code=404,
            detail="Category not found"
        )

    return {
        "message":"Category deleted successfully"
    }