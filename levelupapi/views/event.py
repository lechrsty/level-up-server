"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from levelupapi.models import Event, Gamer, Game


class EventView(ViewSet):
    """Level up game types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single game type

        Returns:
            Response -- JSON serialized game type
        """
        event = Event.objects.get(pk=pk)
        serializer = EventSerializer(event)
        return Response(serializer.data)


    def list(self, request):
        """Handle GET requests to get all game types

        Returns:
            Response -- JSON serialized list of game types
        """
        events = Event.objects.all()

        if "game" in request.query_params:
                query = request.GET.get('game')
                query_int = int(query)
                events = Event.objects.all()
                events = events.filter(game_id=query_int)
        else:
                events = Event.objects.all()

        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized game instance
        """
        gamer = Gamer.objects.get(user=request.auth.user)
        game = Game.objects.get(pk=request.data["game"])

        event = Event.objects.create(
            title=request.data["title"],
            game=game,
            description=request.data["description"],
            organizer=gamer,
            date=request.data["date"],
            time=request.data["time"]
        )
        serializer = EventSerializer(event)
        return Response(serializer.data)

    def update(self, request, pk):

            event = Event.objects.get(pk=pk)
            event.title=request.data["title"]
            event.description=request.data["description"]
            event.date=request.data["date"]
            event.time=request.data["time"]

            game = Game.objects.get(pk=request.data["game"])
            event.game = game

            organizer = Gamer.objects.get(user=request.auth.user)
            event.organizer = organizer

            event.save()

            return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        event = Event.objects.get(pk=pk)
        event.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class EventOrganizerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Gamer
        fields = ('user', 'bio', 'full_name')

class EventGameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Game
        fields = ('id', 'name', 'maker', 'num_of_players', 'skill_level', 'game_type')

class EventSerializer(serializers.ModelSerializer):

    organizer = EventOrganizerSerializer(many=False)
    game = EventGameSerializer(many=False)

    class Meta:
        model = Event
        fields = ('id', 'game', 'title', 'description', 'organizer', 'date', 'time')
        depth = 1