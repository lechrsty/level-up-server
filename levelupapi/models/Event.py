from django.db import models

class Event(models.Model):

    game = models.ForeignKey("Game", on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    organizer = models.ForeignKey("Gamer", on_delete=models.SET_NULL, null=True, related_name="created_events")
    date = models.DateField(auto_now=False)
    time = models.TimeField(auto_now=False)
    attendees = models.ManyToManyField("Gamer", through="GamerEvent")

    @property
    def joined(self):
        return self.__joined

    @joined.setter
    def joined(self, value):
        self.__joined = value


