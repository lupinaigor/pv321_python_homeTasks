from django.urls import path
from .views import PredictionView

urlpatterns = [
    path('get-prediction/', PredictionView.as_view(), name='get-prediction'),
]