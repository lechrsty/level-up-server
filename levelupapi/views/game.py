"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from levelupapi.models import Game, Gamer, GameType


class GameView(ViewSet):

    def retrieve(self, request, pk):

        game = Game.objects.get(pk=pk)
        serializer = GameSerializer(game)
        return Response(serializer.data)


    def list(self, request):

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

    def update(self, request, pk):
            """Handle PUT requests for a game

            Returns:
                Response -- Empty body with 204 status code
            """

            game = Game.objects.get(pk=pk)
            game.name=request.data["name"]
            game.maker=request.data["maker"]
            game.num_of_players=request.data["num_of_players"]
            game.skill_level=request.data["skill_level"]

            game_type = GameType.objects.get(pk=request.data["game_type"])
            game.game_type = game_type

            gamer = Gamer.objects.get(user=request.auth.user)
            game.gamer = gamer

            game.save()

            return Response(None, status=status.HTTP_204_NO_CONTENT)

        
class GameGamerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Gamer
        fields = ('user', 'bio', 'full_name')

class GameSerializer(serializers.ModelSerializer):

    gamer = GameGamerSerializer(many=False)

    class Meta:
        model = Game
        fields = ('id', 'gamer', 'name', 'game_type', 'maker', 'num_of_players', 'skill_level')
        depth = 1
