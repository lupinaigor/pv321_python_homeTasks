from django.urls import path
from .views import RandomNumberView

urlpatterns = [
    # path('get-prediction/', PredictionView.as_view(), name='get-prediction'),
    path('random-number/', RandomNumberView.as_view(), name='random-number'),
]

# Генерація одного числа:
# http://127.0.0.1:8000/api/random-number/
#
# Генерація числа в диапазоне:
# http://127.0.0.1:8000/api/random-number/?mode=range&start=10&end=50
#
# Генерація набора чисел:
# http://127.0.0.1:8000/api/random-number/?mode=set&count=3&start=1&end=100