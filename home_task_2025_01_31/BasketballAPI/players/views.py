from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# словник
players = {
    1: {"name": "Michael Jordan", "height": 198},
    2: {"name": "LeBron James", "height": 206},
    3: {"name": "Kobe Bryant", "height": 198},
}

class PlayerListView(APIView):
    """Обробник списку гравців: отримати всіх та додати нового"""

    def get(self, request):
        return Response(players)

    def post(self, request):
        new_id = max(players.keys(), default=0) + 1  # Генерація нового ID
        players[new_id] = {
            "name": request.data.get("name"),
            "height": request.data.get("height"),
        }
        return Response({"id": new_id, "player": players[new_id]}, status=status.HTTP_201_CREATED)
    

class PlayerDetailView(APIView):
    """Обробник для одного гравця: знайти, оновити, видалити"""

    def get(self, request, player_id):
        player = players.get(player_id)
        if not player:
            return Response({"error": "Player not found"}, status=status.HTTP_404_NOT_FOUND)
        return Response(player)

    def put(self, request, player_id):
        if player_id not in players:
            return Response({"error": "Player not found"}, status=status.HTTP_404_NOT_FOUND)

        players[player_id]["name"] = request.data.get("name", players[player_id]["name"])
        players[player_id]["height"] = request.data.get("height", players[player_id]["height"])

        return Response(players[player_id])

    def delete(self, request, player_id):
        if player_id not in players:
            return Response({"error": "Player not found"}, status=status.HTTP_404_NOT_FOUND)

        del players[player_id]
        return Response({"message": "Player deleted"}, status=status.HTTP_204_NO_CONTENT)
