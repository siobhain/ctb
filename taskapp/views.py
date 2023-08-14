from django.shortcuts import render, HttpResponse
from django.views import generic
from .models import Task


def ctb_welcome(request):
    return HttpResponse("Welcome to CTB app")


# def get_taskapp_list(request):
#     tasks = Task.objects.all()
#     queryset = Task.objects.filter(completed=True)
#     context = {
#         'tasks': tasks
#     }
#     return render(request, 'taskapp/taskapp_list.html', context)

class CompletedTaskList(generic.ListView):
    model = Task
    queryset = Task.objects.filter(completed=True).order_by('-created_on')
    template_name = 'index.html'


class TodoTaskList(generic.ListView):
    model = Task
    queryset = Task.objects.filter(completed=False).order_by('-created_on')
    template_name = 'index.html'
