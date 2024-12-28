class Book:
    def __init__(self, title, year, publisher, genre, author, price):
        self.title = title
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price

    # перевантажені методи
    def __lt__(self, other):
        return self.price < other.price

    def __eq__(self, other):
        return self.price == other.price

    def __gt__(self, other):
        return self.year > other.year



    def display(self):
        print(f"Назва книги: {self.title}")
        print(f"Рік видання: {self.year}")
        print(f"Видавництво: {self.publisher}")
        print(f"Жанр: {self.genre}")
        print(f"Автор: {self.author}")
        print(f"Ціна: {self.price}")

    def input_data(self):
        self.title = input("Введіть назву книги ")
        self.year = int(input("Введіть рік видання "))
        self.publisher = input("Введіть видавництво ")
        self.genre = input("Введіть жанр ")
        self.author = input("Введіть автора ")
        self.price = float(input("Введіть ціну "))




# Створюємо об'ект
book1 = Book("Dandellon Wine", 1982, "Bantam Books", "Fiction", "Ray Bradbury", 2.75)
book2 = Book("Wheels", 1974, "Pan Books", "industrial novel", "Arthur Hailey", 1.80)
# Виводимо дані про книгу
book1.display()
book2.display()

# Змінюємо дані через метод input_data
# print("\nОновимо дані про книгу:")
# book1.input_data()

# Виводимо оновлені дані
print("\nОновлені дані про книгу:")
book1.display()


# Порівняння по ціні
print(book1 < book2)    # False (2.75 > 1.80)
print(book1 == book2)   # False (2.75 > 1.80)

# Порівняння по року видання
print(book1 > book2)    # True (1982 > 1974)

