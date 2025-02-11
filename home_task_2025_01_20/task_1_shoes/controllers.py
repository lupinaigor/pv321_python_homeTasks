from flask import request
from models import Shoes
from views import prepare_response

shoes_collection = []  # Temporary storage for shoe objects

def create_shoe_controller():
    payload = request.json
    shoe = Shoes(
        shoe_type=payload["shoe_type"],
        category=payload["category"],
        color=payload["color"],
        price=payload["price"],
        manufacturer=payload["manufacturer"],
        size=payload["size"],
    )
    shoes_collection.append(shoe)
    return prepare_response(shoe.to_dict(), "success")

def get_shoes_controller():
    return prepare_response([shoe.to_dict() for shoe in shoes_collection], "success")