from fastapi import APIRouter, HTTPException

from app import crud
from app.schemas import SubCategory



router = APIRouter(
    prefix="/subcategories",
    tags=["SubCategories"]
)



# GET ALL SUBCATEGORIES

@router.get("/")
def get_subcategories():

    return crud.get_all_subcategories()



# GET SINGLE SUBCATEGORY

@router.get("/{subcategory_id}")
def get_subcategory(subcategory_id:int):

    subcategory = crud.get_subcategory(subcategory_id)


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



# CREATE SUBCATEGORY

@router.post("/")
def add_subcategory(subcategory:SubCategory):

    result = crud.create_subcategory(subcategory)


    return {

        "message":"Subcategory added successfully",
        "subcategory":result

    }


@router.put("/{subcategory_id}")
def update_subcategory(subcategory_id:int, subcategory:SubCategory):

    result = crud.update_subcategory(
        subcategory_id,
        subcategory
    )


    if result == 0:

        raise HTTPException(
            status_code=404,
            detail="Subcategory not found"
        )


    return {
        "message":"Subcategory updated successfully"
    }



@router.delete("/{subcategory_id}")
def delete_subcategory(subcategory_id:int):

    result = crud.delete_subcategory(subcategory_id)


    if result == 0:

        raise HTTPException(
            status_code=404,
            detail="Subcategory not found"
        )


    return {
        "message":"Subcategory deleted successfully"
    }