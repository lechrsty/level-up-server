from django.db import models
from .GameType import GameType
from .Gamer import Gamer

class Game(models.Model):

    title = models.CharField(max_length=55)
    description = models.CharField(max_length=500)
    game_type = models.ForeignKey(GameType, on_delete=models.SET_NULL, null=True)
    creator = models.ForeignKey(Gamer, on_delete=models.SET_NULL, null=True)
    created_on = models.DateField(auto_now_add=True)
    player_count = models.IntegerField()
    skill_level = models.CharField(max_length=50)

