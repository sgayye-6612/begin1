from pydantic import BaseModel


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