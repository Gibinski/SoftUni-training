from django.http import HttpResponse
from .models import Tasks
from django.shortcuts import render
# Create your views here.

def index(request):
    return HttpResponse("It's works!")

def list_tasks(request):
    all_tasks = Tasks.objects.all()
    output = "; ".join(f"{t.id} {t.title} {t.priority}" for t in all_tasks)
    if not output:
        output = "There ate no created tasks!"
    return HttpResponse(output)


def list_tasks_template(request):
    return render(request, 'tasks.html')
