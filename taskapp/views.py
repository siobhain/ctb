from django.shortcuts import render, HttpResponse, redirect
from django.views import generic
from django.contrib import messages
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

@login_required()
def get_firstname(request):
    profile = Profile.objects.get(user=request.user)
    return(profile.firstname.capitalize())

@login_required()
def get_surname(request):
    profile = Profile.objects.get(user=request.user)
    return(profile.surname.capitalize())

def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        name = get_firstname(request)
        if form.is_valid():
            category = request.POST.get('category')
            task = request.POST.get('description')
            slug = slugify(task)
            created_by = request.user
            Task.objects.create(
                description=task,
                slug = slug,
                category=category, 
                created_by=created_by)
            length = len(task)
            title = task if length < 20 else task[:10] + "..." + task[-10:]
            messages.success(request, f'Thank you {name}, Task \"{title.capitalize()}\" has been added')
            return redirect('/todo/')
        else:
            messages.error(request, f'Error on the create task, Please try again {name}')
            form = TaskForm()
            return render(request, 'taskapp/create_task.html', {'form': form})
    else:
        form = TaskForm()
        return render(request, 'taskapp/create_task.html', {'form': form})

def get_todo_list(request):
    # tasks = Task.objects.filter(completed=False).order_by('-created_on')
    tasks = Task.objects.all()
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


# Same as above but with the Full list of Tasks
class FullTaskList(generic.ListView):
    model = Task
    queryset = Task.objects.all().order_by('-created_on')
    template_name = 'taskapp/full_list.html'

# sob 22/8 Could not get this to work on create_task, Got from DjangoDoc
# fulllist = FullTaskList.as_view()
# return fulllist(request)
# return render(request, 'taskapp/full_list.html', fulllist)