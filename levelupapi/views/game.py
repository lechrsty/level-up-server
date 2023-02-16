"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from levelupapi.models import Game, Gamer, GameType


class GameView(ViewSet):
    """Level up game types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single game type

        Returns:
            Response -- JSON serialized game type
        """
        game = Game.objects.get(pk=pk)
        serializer = GameSerializer(game)
        return Response(serializer.data)


    def list(self, request):
        """Handle GET requests to get all game types

        Returns:
            Response -- JSON serialized list of game types
        """
        games = Game.objects.all()
        serializer = GameSerializer(games, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized game instance
        """
        gamer = Gamer.objects.get(user=request.auth.user)
        game_type = GameType.objects.get(pk=request.data["game_type"])

        game = Game.objects.create(
            gamer=gamer,
            name=request.data["name"],
            game_type=game_type,
            maker=request.data["maker"],
            num_of_players=request.data["num_of_players"],
            skill_level=request.data["skill_level"]
        )
        serializer = GameSerializer(game)
        return Response(serializer.data)
        
class GameSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    # The Meta class hold the configuration for the serializer. We’re telling the serializer to use the Game model and to include the id andlabel fields.

    class Meta:
        model = Game
        fields = ('id', 'gamer', 'name', 'game_type', 'maker', 'num_of_players', 'skill_level')
        depth = 2
