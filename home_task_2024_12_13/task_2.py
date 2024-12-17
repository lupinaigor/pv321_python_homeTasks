class Book:
    def __init__(self, title, year, publisher, genre, author, price):
        self.title = title
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price

    # Метод для вивода даних
    def display(self):
        print(f"Назва книги: {self.title}")
        print(f"Рік видання: {self.year}")
        print(f"Видавництво: {self.publisher}")
        print(f"Жанр: {self.genre}")
        print(f"Автор: {self.author}")
        print(f"Ціна: {self.price}")

    # Метод для ввода даних
    def input_data(self):
        self.title = input("Введіть назву книги ")
        self.year = input("Введіть рік видання ")
        self.publisher = input("Введіть видавництво ")
        self.genre = input("Введіть жанр ")
        self.author = input("Введіть автора ")
        self.price = input("Введіть ціну ")

# Створюємо об'ект
book = Book("Dandellon Wine", 1982, "Bantam Books", "Fiction", "Ray Bradbury", 2.75)
# Виводимо дані про книгу
book.display()

# Змінюємо дані через метод input_data
print("\nОновимо дані про книгу:")
book.input_data()

# Виводимо оновлені дані
print("\nОновлені дані про книгу:")
book.display()