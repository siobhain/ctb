from django.shortcuts import render, HttpResponse
from .models import Task


# Create your views here.
def ctb_welcome(request):
    return HttpResponse("Welcome to CTB app")


def get_taskapp_list(request):
    tasks = Task.objects.all()
    queryset = Task.objects.filter(completed=True)
    context = {
        'tasks': tasks
    }
    return render(request, 'taskapp/taskapp_list.html', context)
