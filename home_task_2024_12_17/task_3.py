class Stadium:
    def __init__(self, name, year, country, city, capacity):
        self.name = name
        self.year = year
        self.country = country
        self.city = city
        self.capacity = capacity

    # Метод для вивода даних
    def display(self):
        print(f"Назва стадіону: {self.name}")
        print(f"Дата відкриття: {self.year}")
        print(f"Країна: {self.country}")
        print(f"Місто: {self.city}")
        print(f"Місткість: {self.capacity}")

    # Метод для ввода даних
    def input_data(self):
        self.name = input("Введіть назву стадіону: ")
        self.year = input("Введіть дату відкртиття: ")
        self.country = input("Введіть країну: ")
        self.city = input("Введіть місто: ")
        self.capacity = input("Введіть місткість: ")


    # Перевантаження для порівняння за місткістю
    def __lt__(self, other):
        return self.capacity < other.capacity

    def __eq__(self, other):
        return self.capacity == other.capacity

    def __gt__(self, other):
        return self.capacity > other.capacity

    # Перевантаження для порівняння за роком відкриття
    def __lt__(self, other):
        return self.year < other.year

    def __eq__(self, other):
        return self.year == other.year

    def __gt__(self, other):
        return self.year > other.year


# Створюємо об'ект
st1 = Stadium("Авангард", 1965, "Україна", "Луцьк", 12000)
st2 = Stadium("НСК Олімпійський", 1923, "Україна", "Київ", 70000)
# Виводимо дані про стадіон
st1.display()
st2.display()

# Змінюємо дані через метод input_data
# print("\nОновимо дані про стадіон:")
# st1.input_data()

# Виводимо оновлені дані
print("\nОновлені дані про стадіон:")
st1.display()

# Порівняння по місткості
print("\nПорівняння по місткості:")
print(st1 < st2)    # True (12000 < 70000)
print(st1 == st2)   # False (12000 != 70000)
print(st1 > st2)    # False (12000 < 70000)

# Порівняння по року відкриття
print("\nПорівняння по року відкриття:")
print(st1 < st2)    # False (1965 > 1923)
print(st1 == st2)   # False (1965 != 1923)
print(st1 > st2)    # True (1965 > 1923)