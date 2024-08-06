from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404, redirect
from .models import Score, GameScore


# Create your views here.
def index(request):
    team = Score.objects.order_by('id')
    recreation = GameScore.objects.order_by('id')
    context = {'team':team, 'recreation':recreation}
    return render(request, "namespace/scoreboard.html", context)

@csrf_exempt
def add_num(request, pk):
    instance = Score.objects.get(pk=pk)
    instance.score += int(request.POST.get('number', 0))
    instance.save()
    context = {'score': instance}
    return redirect('admin:index')
    
@csrf_exempt
def add_gamenum(request, pk):
    instance = GameScore.objects.get(pk=pk)
    instance.score += int(request.POST.get('number', 0))
    instance.save()
    context = {'score': instance}
    return redirect('admin:index')

