from django.db import models

# Create your models here.
class Team(models.Model):
    teamName = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.teamName

class Score(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)

    def __int__(self):
        return self.score

class Member(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    member = models.TextField()

    def __str__(self):
        return self.member

class GameScore(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)

    def __int__(self):
        return self.score