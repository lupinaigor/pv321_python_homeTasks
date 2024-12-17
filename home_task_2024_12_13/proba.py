class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self._model = model
        self.__year = year
        self.color = color


    # геттер для моделі
    @property
    def car_model(self):
        return self._model

    # cеттер для моделі
    @car_model.setter
    def car_model(self, model):
        self._model = model


    # геттер для року
    @property
    def car__year(self):
        return self.__year

    # cеттер для року
    @car__year.setter
    def car__year(self, year):
        self.__year = year

    # # deleter
    # @car_model.deleter
    # def car_model(self):
    #     del self._model

    def display(self):
        print(f"Make:{self.make}\nModel:{self._model}\nColor:{self.color}\nYear:{self.__year}")


# Створюємо объект
car = Car("Toyota", "Corolla", 2023, "Red")
car.display()

# Змінюємо через геттери/сеттери
car.make = "Honda"         # Пряма зміна (make - відкритий атрибут)
car.car_model = "Civic"    # Через сеттер для _model
car.car__year = 2020       # Через сеттер для __year
car.color = "Blue"         # Пряма зміна (make - відкритий атрибут)

# Виводимо змінені дані
print(car.make)            # Honda
print(car.car_model)       # Civic
print(car.car__year)       # 2020
print(car.color)           # Blue

# del car.car_model
# print(car.car_model)