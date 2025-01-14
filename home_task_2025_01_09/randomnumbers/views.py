from .models import RandomNumber
from rest_framework.views import APIView
from rest_framework.response import Response
import random

class RandomNumberView(APIView):
    def get(self, request):
        mode = request.query_params.get('mode', 'single')  # Тип генерації
        result = ""

        if mode == 'range':
            # Генерація числа в диапазоні
            start = int(request.query_params.get('start', 0))
            end = int(request.query_params.get('end', 100))
            number = random.randint(start, end)
            result = str(number)
            RandomNumber.objects.create(mode=mode, result=result)
            return Response({"mode": "range", "number": number})

        elif mode == 'set':
            # Генерація набора чисел
            count = int(request.query_params.get('count', 5))
            start = int(request.query_params.get('start', 0))
            end = int(request.query_params.get('end', 100))
            numbers = [random.randint(start, end) for _ in range(count)]
            result = ','.join(map(str, numbers))
            RandomNumber.objects.create(mode=mode, result=result)
            return Response({"mode": "set", "numbers": numbers})

        else:
            # Генерація одного числа
            number = random.randint(0, 100)
            result = str(number)
            RandomNumber.objects.create(mode=mode, result=result)
            return Response({"mode": "single", "number": number})


