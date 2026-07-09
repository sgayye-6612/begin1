from fastapi import APIRouter, HTTPException

from app import crud
from app.schemas import Order



router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)



# GET ALL ORDERS

@router.get("/")
def get_orders():

    return crud.get_all_orders()



# GET SINGLE ORDER

@router.get("/{order_id}")
def get_order(order_id:int):

    order = crud.get_order(order_id)


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



# CREATE ORDER

@router.post("/")
def add_order(order:Order):

    result = crud.create_order(order)


    return {

        "message":"Order created successfully",
        "order":result

    }


# UPDATE ORDER


@router.put("/{order_id}")
def update_order(order_id:int, order:Order):

    result = crud.update_order(
        order_id,
        order
    )


    if result == 0:

        raise HTTPException(
            status_code=404,
            detail="Order not found"
        )


    return {
        "message":"Order updated successfully"
    }




# DELETE ORDER


@router.delete("/{order_id}")
def delete_order(order_id:int):

    result = crud.delete_order(order_id)


    if result == 0:

        raise HTTPException(
            status_code=404,
            detail="Order not found"
        )


    return {
        "message":"Order deleted successfully"
    }