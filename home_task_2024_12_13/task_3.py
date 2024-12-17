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

# Створюємо об'ект
st = Stadium("Авангард", "1965", "Україна", "Луцьк", 12000)

# Виводимо дані про стадіон
st.display()

# Змінюємо дані через метод input_data
print("\nОновимо дані про стадіон:")
st.input_data()

# Виводимо оновлені дані
print("\nОновлені дані про стадіон:")
st.display()