from django.db import models
from datetime import datetime

# Create your models here.
class Artiste (models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    age = models.IntegerField()
class Song(models.Model):
    Artiste = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    title = models.CharField(max_length = 400)
    date_released = models.DateField(default = datetime.today)
    likes = models.IntegerField()
    artiste_id = models.CharField(max_length = 50)

class Lyric(models.Model):
    Song = models.ForeignKey(Song, on_delete=models.CASCADE)
    content = models.CharField(max_length = 400)
    song_id = models.CharField(max_length = 50)

