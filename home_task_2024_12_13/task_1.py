class Car:
    def __init__(self, make, model, year, engine_capacity, color, price):
        self.make = make                   # Виробник
        self._model = model                # Модель
        self.__year = year                 # Рік випуску
        self.engine_capacity = engine_capacity  # Об'єм двигуна
        self.color = color                 # Колір
        self.price = price                 # Ціна

    # Геттер и сеттер для моделі
    @property
    def car_model(self):
        return self._model

    @car_model.setter
    def car_model(self, model):
        self._model = model

    # Геттер и сеттер для року
    @property
    def car_year(self):
        return self.__year

    @car_year.setter
    def car_year(self, year):
        self.__year = year

    # Метод для вивода даних
    def display(self):
        print(f"Виробник: {self.make}")
        print(f"Модель: {self.car_model}")
        print(f"Рік випуску: {self.car_year}")
        print(f"Об'єм двигуна: {self.engine_capacity} л")
        print(f"Колір: {self.color}")
        print(f"Ціна: {self.price} $")

    # Метод для ввода даних
    def input_data(self):
        self.make = input("Введіть виробника: ")
        self.car_model = input("Введіть модель: ")
        self.car_year = int(input("Введіть рік випуску: "))
        self.engine_capacity = float(input("Введіть об'єм двигуна (л): "))
        self.color = input("Введіть колір: ")
        self.price = float(input("Введіть ціну ($): "))


# Створюємо об'ект
car = Car("Toyota", "Corolla", 2023, 1.8, "Red", 20000)

# Виводимо дані про автомобіль
car.display()

# Змінюємо дані через метод input_data
print("\nОновимо дані про автомобіль:")
car.input_data()

# Виводимо оновлені дані
print("\nОновлені дані про автомобіль:")
car.display()