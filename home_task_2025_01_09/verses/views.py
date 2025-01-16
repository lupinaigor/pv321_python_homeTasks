from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Verse
import random

class RandomVerseView(APIView):
    def get(self, request):
        verse = random.choice(Verse.objects.all())
        return Response({
            "title": verse.title,
            "author": verse.author,
            "text": verse.text,
            "theme": verse.theme
        })

class RandomAuthorVerseView(APIView):
    def get(self, request):
        author = request.query_params.get('author')
        verses = Verse.objects.filter(author__iexact=author)
        if verses.exists():
            verse = random.choice(verses)
            return Response({
                "title": verse.title,
                "author": verse.author,
                "text": verse.text,
                "theme": verse.theme
            })
        return Response({"error": "Author not found"}, status=404)

class RandomThemeVerseView(APIView):
    def get(self, request):
        theme = request.query_params.get('theme')
        verses = Verse.objects.filter(theme=theme)
        if verses.exists():
            verse = random.choice(verses)
            return Response({
                "title": verse.title,
                "author": verse.author,
                "text": verse.text,
                "theme": verse.theme
            })
        return Response({"error": "Theme not found"}, status=404)

class AuthorVersesView(APIView):
    def get(self, request):
        author = request.query_params.get('author')
        if not author:
            return Response({"error": "Author parameter is required"}, status=400)
        verses = Verse.objects.filter(author__iexact=author)
        if verses.exists():
            titles = [verse.title for verse in verses]
            return Response({
                "author": author,
                "titles": titles
            })
        return Response({"error": "Author not found"}, status=404)


class AllAuthorsView(APIView):
    def get(self, request):
        authors = Verse.objects.values_list('author', flat=True).distinct()
        return Response({"authors": list(authors)})


class AllThemesView(APIView):
    def get(self, request):
        themes = dict(Verse.THEMES).values()
        return Response({"themes": list(themes)})


class TitlesByThemeView(APIView):
    def get(self, request):
        theme = request.query_params.get('theme')
        if not theme:
            return Response({"error": "Theme parameter is required"}, status=400)
        verses = Verse.objects.filter(theme=theme)
        if verses.exists():
            titles = [verse.title for verse in verses]
            return Response({
                "theme": theme,
                "titles": titles
            })
        return Response({"error": "Theme not found"}, status=404)

