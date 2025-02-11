from flask import Flask
from controllers import create_shoe_controller, get_shoes_controller

app = Flask(__name__)

app.add_url_rule("/shoes", "create_shoe", create_shoe_controller, methods=["POST"])
app.add_url_rule("/shoes", "get_shoes", get_shoes_controller, methods=["GET"])



if __name__ == "__main__":
    app.run(debug=True)