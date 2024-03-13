from django.db import models

# Create your models here.
class Team(models.Model):
    teamName = models.CharField(max_length=20)
    pubDate = models.DateTimeField("date published")

    def __str__(self) -> str:
        return self.teamName

class Score(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)

    def __int__(self):
        return self.score