from django.contrib import admin

# Register your models here.
from .models import Team, Score, Member

admin.site.register(Team)

@admin.site.register(Score)
class ScoreAdmin(admin.ModelAdmin):
    list_display('id','team.name','')
admin.site.register(Member)
