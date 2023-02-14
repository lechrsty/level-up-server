from django.db import models

class GameType(models.Model):
    
    category = models.CharField(max_length=55)