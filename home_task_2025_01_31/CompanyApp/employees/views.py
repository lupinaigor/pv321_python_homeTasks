from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# cловник
employees_data = {
    "ivanov": {
        "name": "Іванов Іван Іванович",
        "phone": "+380501234567",
        "email": "ivanov@company.com",
        "position": "Менеджер",
        "office_number": "101",
        "skype": "ivanov_101"
    },
    "petrov": {
        "name": "Петров Петро Петрович",
        "phone": "+380502345678",
        "email": "petrov@company.com",
        "position": "Розробник",
        "office_number": "102",
        "skype": "petrov_102"
    }
}

class EmployeesView(APIView):
    # Отримати список усіх співробітників або інформацію про конкретного співробітника
    def get(self, request, username=None):
        if username:
            employee = employees_data.get(username.lower())
            if employee:
                return Response({username: employee}, status=status.HTTP_200_OK)
            return Response({"error": "Співробітника не знайдено"}, status=status.HTTP_404_NOT_FOUND)
        return Response(employees_data, status=status.HTTP_200_OK)

    # Додати нового співробітника
    def post(self, request):
        username = request.data.get("username")
        if not username or username.lower() in employees_data:
            return Response({"error": "Некоректний або вже існуючий username"}, status=status.HTTP_400_BAD_REQUEST)

        employees_data[username.lower()] = {
            "name": request.data.get("name"),
            "phone": request.data.get("phone"),
            "email": request.data.get("email"),
            "position": request.data.get("position"),
            "office_number": request.data.get("office_number"),
            "skype": request.data.get("skype")
        }
        return Response({"message": "Співробітника додано", username: employees_data[username.lower()]}, status=status.HTTP_201_CREATED)

    # Змінити дані співробітника
    def put(self, request, username):
        if username.lower() not in employees_data:
            return Response({"error": "Співробітника не знайдено"}, status=status.HTTP_404_NOT_FOUND)

        for key in request.data:
            employees_data[username.lower()][key] = request.data[key]

        return Response({"message": "Дані оновлені", username: employees_data[username.lower()]}, status=status.HTTP_200_OK)

    # Видалити співробітника
    def delete(self, request, username):
        if username.lower() not in employees_data:
            return Response({"error": "Співробітника не знайдено"}, status=status.HTTP_404_NOT_FOUND)

        del employees_data[username.lower()]
        return Response({"message": "Співробітника видалено"}, status=status.HTTP_200_OK)
