from django.db import models
from .GameType import GameType
from .Gamer import Gamer

class Game(models.Model):

    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    name = models.CharField(max_length=55)
    game_type = models.ForeignKey("GameType", on_delete=models.SET_NULL, null=True)
    maker = models.CharField(max_length=500)
    num_of_players = models.IntegerField()
    skill_level = models.CharField(max_length=50)

