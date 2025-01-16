from django.urls import path
from .views import RandomVerseView, RandomAuthorVerseView, RandomThemeVerseView

urlpatterns = [
    path('random-verse/', RandomVerseView.as_view(), name='random-verse'),
    path('random-author-verse/', RandomAuthorVerseView.as_view(), name='random-author-verse'),
    path('random-theme-verse/', RandomThemeVerseView.as_view(), name='random-theme-verse'),
]

# Випадковий вірш:
# http://127.0.0.1:8000/api/verses/random-verse/
#
# Випадковий вірш автора:
# http://127.0.0.1:8000/api/verses/random-author-verse/?author=Тарас%20Шевченко
#
# Випадковий вірш за тематикою:
# http://127.0.0.1:8000/api/verses/random-theme-verse/?theme=love
