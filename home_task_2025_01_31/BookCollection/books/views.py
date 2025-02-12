from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Словник
books_data = {
    "1984": {
        "author": "Джордж Оруелл",
        "title": "1984",
        "genre": "Антиутопія",
        "year": 1949,
        "pages": 328,
        "publisher": "Сейкер & Уорбург"
    },
    "war_and_peace": {
        "author": "Лев Толстой",
        "title": "Война и мир",
        "genre": "Роман",
        "year": 1869,
        "pages": 1225,
        "publisher": "Художня Література"
    }
}

class BooksView(APIView):
    # Отримати список усіх книг або конкретну книгу
    def get(self, request, book_id=None):
        if book_id:
            book = books_data.get(book_id.lower())
            if book:
                return Response({book_id: book}, status=status.HTTP_200_OK)
            return Response({"error": "Книгу не знайдено"}, status=status.HTTP_404_NOT_FOUND)
        return Response(books_data, status=status.HTTP_200_OK)

    # Додати нову книгу
    def post(self, request):
        book_id = request.data.get("book_id")
        if not book_id or book_id.lower() in books_data:
            return Response({"error": "Некоректний чи вже існуючий ідентифікатор книги"}, status=status.HTTP_400_BAD_REQUEST)

        books_data[book_id.lower()] = {
            "author": request.data.get("author"),
            "title": request.data.get("title"),
            "genre": request.data.get("genre"),
            "year": request.data.get("year"),
            "pages": request.data.get("pages"),
            "publisher": request.data.get("publisher")
        }
        return Response({"message": "Книга додана", book_id: books_data[book_id.lower()]}, status=status.HTTP_201_CREATED)

    # Змінити дані книги
    def put(self, request, book_id):
        if book_id.lower() not in books_data:
            return Response({"error": "Книгу не знайдено"}, status=status.HTTP_404_NOT_FOUND)

        for key in request.data:
            books_data[book_id.lower()][key] = request.data[key]

        return Response({"message": "Дані оновлено", book_id: books_data[book_id.lower()]}, status=status.HTTP_200_OK)

    # Видалити книгу
    def delete(self, request, book_id):
        if book_id.lower() not in books_data:
            return Response({"error": "Книгу не знайдено"}, status=status.HTTP_404_NOT_FOUND)

        del books_data[book_id.lower()]
        return Response({"message": "Книгу видалено"}, status=status.HTTP_200_OK)
