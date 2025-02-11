class Recipe:
    def __init__(self, name, author, recipe_type, description, video_link, ingredients, cuisine):
        self.name = name
        self.author = author
        self.recipe_type = recipe_type  # e.g., "Main Course", "Dessert"
        self.description = description
        self.video_link = video_link
        self.ingredients = ingredients  # List of ingredients
        self.cuisine = cuisine  # e.g., "Italian", "Ukrainian"

    def to_dict(self):
        return {
            "name": self.name,
            "author": self.author,
            "recipe_type": self.recipe_type,
            "description": self.description,
            "video_link": self.video_link,
            "ingredients": self.ingredients,
            "cuisine": self.cuisine,
        }

    def update_from_dict(self, data):
        self.name = data.get("name", self.name)
        self.author = data.get("author", self.author)
        self.recipe_type = data.get("recipe_type", self.recipe_type)
        self.description = data.get("description", self.description)
        self.video_link = data.get("video_link", self.video_link)
        self.ingredients = data.get("ingredients", self.ingredients)
        self.cuisine = data.get("cuisine", self.cuisine)