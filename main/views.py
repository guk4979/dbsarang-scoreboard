from django.shortcuts import render
from django.views.generic import ListView
from .models import Score


# Create your views here.
def index(request):
    team = Score.objects.order_by('id')
    context = {'team':team}
    return render(request, "namespace/scoreboard.html", context)
