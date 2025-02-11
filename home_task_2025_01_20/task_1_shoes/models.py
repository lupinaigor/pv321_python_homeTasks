class Shoes:
    def __init__(self, shoe_type, category, color, price, manufacturer, size):
        self.shoe_type = shoe_type  # male or female
        self.category = category  # sneakers, boots, sandals, shoes
        self.color = color
        self.price = price
        self.manufacturer = manufacturer
        self.size = size

    def to_dict(self):
        return {
            "shoe_type": self.shoe_type,
            "category": self.category,
            "color": self.color,
            "price": self.price,
            "manufacturer": self.manufacturer,
            "size": self.size,
        }

    def update_from_dict(self, data):
        self.shoe_type = data.get("shoe_type", self.shoe_type)
        self.category = data.get("category", self.category)
        self.color = data.get("color", self.color)
        self.price = data.get("price", self.price)
        self.manufacturer = data.get("manufacturer", self.manufacturer)
        self.size = data.get("size", self.size)
