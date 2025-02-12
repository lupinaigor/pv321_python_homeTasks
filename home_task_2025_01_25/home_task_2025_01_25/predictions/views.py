from rest_framework.views import APIView
from rest_framework.response import Response
import random

class PredictionView(APIView):
    def get(self, request):
        predictions = [
            "Сьогодні твій день!",
            "Успіх посміхається наполегливим.",
            "Чекай хороших новин.",
            "Все буде добре!",
            "Час діяти!"
        ]
        prediction = random.choice(predictions)
        return Response({"prediction": prediction})