from django.db import models
from .Gamer import Gamer
from .Game import Game


class Event(models.Model):
    
    game = models.ForeignKey(Game, on_delete=models.SET_NULL, null=True)
    description = models.CharField(max_length=200)
    organizer = models.ForeignKey(Gamer, on_delete=models.SET_NULL, null=True)
    date = models.DateField(auto_now=False)
    time = models.TimeField(auto_now=False)
    joined = models.BooleanField(None)
    