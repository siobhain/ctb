from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.views import generic
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.template.defaultfilters import slugify
from .models import Task, Profile
from .forms import TaskForm


# ctb_welcome
# This is where it all begins!! Well rendering either of the 2 home pages
# This ctb_welcome function will launch the members homepage (home_member.html)
# if a user is logged in - Decorator login_required is what takes care of this
# & if no user is logged in the guest will be redirected according to the
# LOGIN_URL in settings.py which is 'guest/' & this url is routed to the
# the CBV GuestCompletedList below => home_guest.html
@login_required()
def ctb_welcome(request):
    firstname = get_firstname(request)
    tasks = Task.objects.filter(completed=False).filter(status=1).order_by('-created_on')
    context = {
        'tasks': tasks
    }
    return render(request, 'taskapp/home_member.html', context)


@login_required()
def get_firstname(request):
    profile = Profile.objects.get(user=request.user)
    return (profile.firstname.capitalize())


@login_required()
def get_surname(request):
    profile = Profile.objects.get(user=request.user)
    return (profile.surname.capitalize())

# create_task : Have to be  alogged in user to use thi view
#
# If its POST then user has already filled out the form
# Otherwise its 1st pass thru this view and user has just 
# requested to add a new task, so need an instance of TaskForm
# send to the template create_task.html for render to user
#
# So with POST need to check form is_valid & if not send 
# an error message to the user to try again
# Once form is_valid Create a new Task with the info provided
# & send Thanks you message to user
@login_required()
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
                slug=slug,
                category=category,
                created_by=created_by)
            length = len(task)
            title = task if length <= 20 else task[:10] + "..." + task[-10:]
            messages.success(request, f'Thank you {name}, Task \"{title.capitalize()}\" has been added')
            return redirect('/todo/')
        else:
            messages.error(request, f'Error adding a  task, Please try again {name}')
            form = TaskForm()
            return render(request, 'taskapp/create_task.html', {'form': form})
    else:
        form = TaskForm()
        return render(request, 'taskapp/create_task.html', {'form': form, })


# edit_task : Can only edit Task created_by yourself
#
# If its POST then user has already entered data
# Otherwise its 1st pass thru this view and user has just 
# requested to update a task passing the task_id, Details 
# of the particular Task already retrieved from the database with
# get_object_or_404, an instance of TaskForm is populated with 
# the task details and this context is sent to template
# edit_task.html for render to user, Also added extra variable
# created_by to context for client side defensive check in template
# as unable to get defensive checks at server level working correctly
# ie login_required decorator on edit_task caused server errors
#
# With POST need to check form is_valid & if not return to
# the todo page, Once form is_valid save the updated details
# & send success message to user
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    description = task.description
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            task = form.cleaned_data['description']
            length = len(task)
            title = description if length <= 25 else task[:10] + "..." + task[-10:]
            name = get_firstname(request)
            messages.success(request, f'{name}, Update(s) to this Task \"{title.capitalize()}\" are reflected on the board')
        return redirect('/todo/')
    form = TaskForm(instance=task)
    created_by = task.created_by
    context = {
        'form': form,
        'created_by': created_by,
    }
    return render(request, 'taskapp/edit_task.html', context)
# edit_task could be further refined by having separate
# CTA buttons/links for
#   Marking a Task as Done ie Conpleted
#   Changing the Category choice
#   Option to undo Conpleted tickbox


# delete task is rudimentary, unable to get modal to work, had to revert
@login_required()
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    description = task.description
    name = get_firstname(request)
    if task.created_by == request.user:
        messages.success(request, f'{name}, You have REMOVED this Task \"{description.capitalize()}\"')
        task.delete()
    else:
        messages.warning(request, "You can only remove a Task that was created by YOU")
    return redirect('/todo')


# get_todo_list : List of Tasks created by the logged in user & that are NOT completed
@login_required()
def get_todo_list(request):
    tasks = Task.objects.filter(created_by=request.user).filter(completed=False).order_by('-created_on')
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
    queryset = Task.objects.filter(completed=True).filter(status=1).order_by('-modified_on')
    template_name = 'taskapp/home_guest.html'


# MemberTodoList : A class based view that inherits from ListView
# Used to display a list of Task objects that are not completed (False)
# this view is rendered by the home_member.html template
# & is what logged in members can see for their home
class MemberTodoList(generic.ListView):
    model = Task
    queryset = Task.objects.filter(completed=False).order_by('-created_on')
    template_name = 'taskapp/home_member.html'


# FullTasklist : Same as above but with the Full list of Tasks,  
# Used in topbox button in home_member.html
# view rendered by full_list.html
class FullTaskList(generic.ListView):
    model = Task
    queryset = Task.objects.filter(status=1).order_by('-created_on')
    template_name = 'taskapp/full_list.html'
