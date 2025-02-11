from django.urls import path
from .views import (
    RandomVerseView, RandomAuthorVerseView, RandomThemeVerseView,
    AuthorVersesView, AllAuthorsView, AllThemesView, TitlesByThemeView
)

urlpatterns = [
    path('random-verse/', RandomVerseView.as_view(), name='random-verse'),
    path('random-author-verse/', RandomAuthorVerseView.as_view(), name='random-author-verse'),
    path('random-theme-verse/', RandomThemeVerseView.as_view(), name='random-theme-verse'),
    path('author-verses/', AuthorVersesView.as_view(), name='author-verses'),
    path('all-authors/', AllAuthorsView.as_view(), name='all-authors'),
    path('all-themes/', AllThemesView.as_view(), name='all-themes'),
    path('titles-by-theme/', TitlesByThemeView.as_view(), name='titles-by-theme'),
]

