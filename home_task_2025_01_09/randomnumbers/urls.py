from django.urls import path
from .views import RandomNumberView

urlpatterns = [
    # path('get-prediction/', PredictionView.as_view(), name='get-prediction'),
    path('random-number/', RandomNumberView.as_view(), name='random-number'),
]