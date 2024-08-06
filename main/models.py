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


class GameScore(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)

    def __int__(self):
        return self.score


# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

@receiver(post_save, sender=Team)
def create_related_model(sender, instance, created, **kwargs):
    if created:  # PrimaryModel 인스턴스가 처음 생성된 경우에만
        Score.objects.create(team=instance)
        GameScore.objects.create(team=instance)

@receiver(post_save, sender=Score)
def score_update(sender, instance, **kwargs):
    channel_layer = get_channel_layer()
    message = f"Model instance {instance} was saved."

    # WebSocket에 메시지를 보내기 위해 채널을 통해 메시지를 전송합니다
    async_to_sync(channel_layer.group_send)(
        'score_update',
        {
            'type': 'send_message',
            'message': message,
        }
    )

@receiver(post_save, sender=GameScore)
def score_update(sender, instance, **kwargs):
    channel_layer = get_channel_layer()
    message = f"Model instance {instance} was saved."

    # WebSocket에 메시지를 보내기 위해 채널을 통해 메시지를 전송합니다
    async_to_sync(channel_layer.group_send)(
        'score_update',
        {
            'type': 'send_message',
            'message': message,
        }
    )