from fastapi import APIRouter, HTTPException

from app import crud
from app.schemas import Customer


router = APIRouter(
    prefix="/customers",
    tags=["Customers"]
)



@router.get("/")
def get_customers():

    return crud.get_all_customers()



@router.get("/{customer_id}")
def get_customer(customer_id:int):

    customer = crud.get_customer(customer_id)


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



@router.post("/")
def add_customer(customer:Customer):

    result = crud.create_customer(customer)


    return {

        "message":"Customer added successfully",
        "customer":result

    }

# UPDATE CUSTOMER


@router.put("/{customer_id}")
def update_customer(customer_id:int, customer:Customer):

    result = crud.update_customer(
        customer_id,
        customer
    )


    if result == 0:

        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )


    return {
        "message":"Customer updated successfully"
    }




# DELETE CUSTOMER


@router.delete("/{customer_id}")
def delete_customer(customer_id:int):

    result = crud.delete_customer(customer_id)


    if result == 0:

        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )


    return {
        "message":"Customer deleted successfully"
    }