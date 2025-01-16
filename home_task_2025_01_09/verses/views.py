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

