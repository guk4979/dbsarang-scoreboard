from django.contrib import admin
from django.views.generic import ListView

# Register your models here.
from .models import Team, Score, GameScore



admin.site.register(Team)

class ScoreAdmin(admin.ModelAdmin):
    change_form_template = 'admin/Score/change_form.html'
    list_display = ('team','score')
admin.site.register(Score, ScoreAdmin)
class GameScoreAdmin(admin.ModelAdmin):
    change_form_template = 'admin/Score/change_form.html'
    list_display = ('team','score')

admin.site.register(GameScore, GameScoreAdmin)