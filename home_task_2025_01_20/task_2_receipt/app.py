from flask import Flask
from controllers import create_recipe_controller, get_recipes_controller

app = Flask(__name__)

# Add routes
app.add_url_rule("/recipes", "create_recipe", create_recipe_controller, methods=["POST"])
app.add_url_rule("/recipes", "get_recipes", get_recipes_controller, methods=["GET"])

if __name__ == "__main__":
    app.run(debug=True)