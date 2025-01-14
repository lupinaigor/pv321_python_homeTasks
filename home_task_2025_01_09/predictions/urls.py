# from django.urls import path
# from . import views
#
# urlpatterns = [
#     path('prediction/', views.get_prediction, name='get_prediction'),
# ]


from django.urls import path
from .views import PredictionView

urlpatterns = [
    path('get-prediction/', PredictionView.as_view(), name='get-prediction'),
]