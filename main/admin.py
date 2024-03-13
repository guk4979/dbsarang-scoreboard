from django.contrib import admin

# Register your models here.
from .models import Team, Score

admin.site.register(Team)
admin.site.register(Score)
