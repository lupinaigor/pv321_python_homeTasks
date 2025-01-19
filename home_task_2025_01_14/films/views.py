import requests
from functools import wraps
from django.shortcuts import render
from django.http import JsonResponse

BASE_URL = "https://swapi.dev/api"

def fetch_data(endpoint):
    """
    Декоратор для виконання запитів до API.
    """
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            url = f"{BASE_URL}/{endpoint}"
            if 'id' in kwargs:
                url = f"{url}/{kwargs['id']}/"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                return view_func(request, data, *args, **kwargs)
            else:
                return JsonResponse({'error': 'Failed to fetch data from API'}, status=response.status_code)
        return wrapper
    return decorator

@fetch_data("films")
def films_list(request, data):
    """
    Представлення для відображення списка фильмів.
    """
    films = data.get('results', [])
    return render(request, 'films/films_list.html', {'films': films})

@fetch_data("films")
def film_detail(request, data, id):
    """
    Представлення для відображення информації про конкретний фільм.
    """
    return render(request, 'films/film_detail.html', {'film': data})



@fetch_data("people")
def characters_list(request, data):
    """
    Представлення для відображення списка персонажів.
    """
    characters = data.get('results', [])
    return render(request, 'films/characters_list.html', {'characters': characters})

@fetch_data("people")
def character_detail(request, data, id):
    """
    Представлення для відображення информації про конкретного персонажа.
    """
    return render(request, 'films/character_detail.html', {'character': data})



@fetch_data("planets")
def planets_list(request, data):
    """
    Представление для отображения списка планет.
    """
    planets = data.get('results', [])
    return render(request, 'films/planets_list.html', {'planets': planets})

@fetch_data("planets")
def planet_detail(request, data, id):
    """
    Представление для отображения информации о конкретной планете.
    """
    return render(request, 'films/planet_detail.html', {'planet': data})
