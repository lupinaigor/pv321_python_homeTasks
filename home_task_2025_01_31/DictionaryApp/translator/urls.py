from django.urls import path
from .views import DictionaryView

urlpatterns = [
    path('dictionary/', DictionaryView.as_view(), name='dictionary'),
    path('dictionary/<str:word>/', DictionaryView.as_view(), name='dictionary_detail'),
]