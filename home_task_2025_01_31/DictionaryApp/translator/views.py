from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Словник
dictionary = {
    "hello": "bonjour",
    "goodbye": "au revoir",
    "please": "s'il vous plaît",
    "thank you": "merci"
}


class DictionaryView(APIView):
    # Отримання перекладу слова
    def get(self, request, word=None):
        if word:
            translation = dictionary.get(word.lower())
            if translation:
                return Response({word: translation}, status=status.HTTP_200_OK)
            return Response({"error": "Слово не знайдено"}, status=status.HTTP_404_NOT_FOUND)
        return Response(dictionary, status=status.HTTP_200_OK)

    # Додавання нового слова
    def post(self, request):
        word = request.data.get("word")
        translation = request.data.get("translation")

        if not word or not translation:
            return Response({"error": "Необхідно вказати слово та переклад"}, status=status.HTTP_400_BAD_REQUEST)

        dictionary[word.lower()] = translation.lower()
        return Response({"message": "Слово додано", word: translation}, status=status.HTTP_201_CREATED)

    # Зміна перекладу слова
    def put(self, request, word):
        if word.lower() not in dictionary:
            return Response({"error": "Слово не знайдено"}, status=status.HTTP_404_NOT_FOUND)

        new_translation = request.data.get("translation")
        if not new_translation:
            return Response({"error": "Необхідно вказати новий переклад"}, status=status.HTTP_400_BAD_REQUEST)

        dictionary[word.lower()] = new_translation.lower()
        return Response({"message": "Переклад змінено", word: new_translation}, status=status.HTTP_200_OK)

    # Видалення слова
    def delete(self, request, word):
        if word.lower() not in dictionary:
            return Response({"error": "Слово не знайдено"}, status=status.HTTP_404_NOT_FOUND)

        del dictionary[word.lower()]
        return Response({"message": "Слово видалено"}, status=status.HTTP_200_OK)
