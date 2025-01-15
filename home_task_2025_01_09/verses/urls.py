from django.urls import path
from .views import RandomVerseView, RandomAuthorVerseView, RandomThemeVerseView

urlpatterns = [
    path('random-verse/', RandomVerseView.as_view(), name='random-verse'),
    path('random-author-verse/', RandomAuthorVerseView.as_view(), name='random-author-verse'),
    path('random-theme-verse/', RandomThemeVerseView.as_view(), name='random-theme-verse'),
]
