from rest_framework.views import APIView
from rest_framework.response import Response
import random

class PredictionView(APIView):
    def get(self, request):
        predictions = [
            "Разом ми подолаємо всі труднощі.",
            "Новий день приносить нові можливості.",
            "Кожна маленька дія наближає велику перемогу.",
            "Не бійся змін, вони ведуть до кращого.",
            "Сила в правді, а правда завжди з нами."
        ]
        prediction = random.choice(predictions)
        return Response({"prediction": prediction})