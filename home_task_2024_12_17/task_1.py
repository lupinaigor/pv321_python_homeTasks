class Car:
    def __init__(self, make, model, year, engine_capacity, color, price):
        self.make = make
        self.model = model
        self.year = year
        self.engine_capacity = engine_capacity
        self.color = color
        self.price = price


    # Метод для вивода даних
    def display(self):
        print(f"Виробник: {self.make}")
        print(f"Модель: {self.model}")
        print(f"Рік випуску: {self.year}")
        print(f"Об'єм двигуна: {self.engine_capacity} л")
        print(f"Колір: {self.color}")
        print(f"Ціна: {self.price} $")

    # Метод для ввода даних
    def input_data(self):
        self.make = input("Введіть виробника: ")
        self.model = input("Введіть модель: ")
        self.year = int(input("Введіть рік випуску: "))
        self.engine_capacity = float(input("Введіть об'єм двигуна (л): "))
        self.color = input("Введіть колір: ")
        self.price = float(input("Введіть ціну ($): "))



    # Перевантаження для порівняння за ціною
    def __lt__(self, other):
        return self.price < other.price

    def __eq__(self, other):
        return self.price == other.price

    def __gt__(self, other):
        return self.price > other.price

    # Перевантаження для порівняння за роком випуску
    def __lt__(self, other):
        return self.year < other.year

    def __eq__(self, other):
        return self.year == other.year

    def __gt__(self, other):
        return self.year > other.year


# Створюємо об'ект
car1 = Car("Toyota", "Corolla", 2023, 1.8, "Red", 20000)
car2 = Car("BMW", "x5", 2020, 3.0, "Black", 30000)

# Виводимо дані про автомобіль
car1.display()
car2.display()

# Змінюємо дані через метод input_data
# print("\nОновимо дані про автомобіль:")
# car1.input_data()

# Виводимо оновлені дані
print("\nОновлені дані про автомобіль:")
car1.display()


print("\nПорівняння по ціні:")
print(car1 < car2)    # False (20000 < 30000)
print(car1 == car2)   # False (20000 != 30000)
print(car1 > car2)    # True (20000 > 30000)


print("\nПорівняння по року випуску:")
print(car1 < car2)    # False (2023 > 2020)
print(car1 == car2)   # False (2023 != 2020)
print(car1 > car2)    # True (2023 > 2020)