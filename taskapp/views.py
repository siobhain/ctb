from django.shortcuts import render, HttpResponse, redirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.template.defaultfilters import slugify
from .models import Task, Profile
from .forms import TaskForm

# from django.contrib.messages import get_messages

# storage = get_messages(request)
# for message in storage:
#     do_something_with_the_message(message)


# This is where it all begins!! Well picking iether of the 2 home pages 
# This ctb_welcome function will launch the members homepage (home_member.html)
# once a user is logged in - Decorator login_required is what takes care of this
# & if no user is logged in the guest will be redirected according to the
# LOGIN_URL in settings.py which is 'guest/' & this url is routed to the
# the CBV GuestCompletedList below => home_guest.html

@login_required()
def ctb_welcome(request):
    user = request.user
    # profile = 
    return render(request, 'taskapp/home_member.html')


def create_task(request):
    if request.method == 'POST':
        category = request.POST.get('category')
        description = request.POST.get('description')
        slug = slugify(description)
        created_by = request.user
        Task.objects.create(
            description=description, 
            slug = slug,
            category=category, 
            created_by=created_by
            )
        # return redirect('get_todo_list')
        return render(request, 'taskapp/todo_list.html')
    else:
        form = TaskForm()
        return render(request, 'taskapp/create_task.html', {'form': form})

def get_todo_list(request):
    # model = Task
    tasks = Task.objects.all()
    queryset = Task.objects.filter(completed=False)
    context = {
        'tasks': tasks
    }
    return render(request, 'taskapp/todo_list.html', context)


# GuestCompletedList : A class based view (CBV) that inherits from ListView
# Used to display a list of Task objects that are completed (True)
# this view is rendered by the home_guest.html template
# & is what general public / guests can see on Guest home page
class GuestCompletedList(generic.ListView):
    model = Task
    queryset = Task.objects.filter(completed=True).order_by('-created_on')
    template_name = 'taskapp/home_guest.html'


# MemberTodoList : A class based view that inherits from ListView
# Used to display a list of Task objects that are not completed (False)
# this view is rendered by the home_member.html template
# & is what logged in members can see for their home
class MemberTodoList(generic.ListView):
    model = Task
    queryset = Task.objects.filter(completed=False).order_by('-created_on')
    template_name = 'taskapp/home_member.html'
