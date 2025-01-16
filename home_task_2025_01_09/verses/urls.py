from django.urls import path
from .views import RandomVerseView, RandomAuthorVerseView, RandomThemeVerseView, AllAuthorsView, AllThemesView, \
    TitlesByThemeView

urlpatterns = [
    path('random-verse/', RandomVerseView.as_view(), name='random-verse'),
    path('random-author-verse/', RandomAuthorVerseView.as_view(), name='random-author-verse'),
    path('random-theme-verse/', RandomThemeVerseView.as_view(), name='random-theme-verse'),
    path('all-authors/', AllAuthorsView.as_view(), name='all-authors'),
    path('all-themes/', AllThemesView.as_view(), name='all-themes'),
    path('titles-by-theme/', TitlesByThemeView.as_view(), name='titles-by-theme'),
]

# Випадковий вірш:
# http://127.0.0.1:8000/api/verses/random-verse/
#
# Випадковий вірш автора:
# http://127.0.0.1:8000/api/verses/random-author-verse/?author=Тарас%20Шевченко
#
# Випадковий вірш за тематикою:
# http://127.0.0.1:8000/api/verses/random-theme-verse/?theme=love



# Назви усіх віршів автора:
# GET http://127.0.0.1:8000/api/verses/author-verses/?author=Тарас%20Шевченко
#
# Список усіх авторів:
# GET http://127.0.0.1:8000/api/verses/all-authors/
#
# Список усіх тематик:
# GET http://127.0.0.1:8000/api/verses/all-themes/
#
# Назви усіх віршів за вказаною тематикою:
# GET http://127.0.0.1:8000/api/verses/titles-by-theme/?theme=love


