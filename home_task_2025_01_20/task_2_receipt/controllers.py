from flask import request
from models import Recipe
from views import prepare_response

recipe_collection = []  # Temporary storage for recipe objects

def create_recipe_controller():
    payload = request.json
    recipe = Recipe(
        name=payload["name"],
        author=payload["author"],
        recipe_type=payload["recipe_type"],
        description=payload["description"],
        video_link=payload["video_link"],
        ingredients=payload["ingredients"],
        cuisine=payload["cuisine"],
    )
    recipe_collection.append(recipe)
    return prepare_response(recipe.to_dict(), "success")

def get_recipes_controller():
    return prepare_response([recipe.to_dict() for recipe in recipe_collection], "success")