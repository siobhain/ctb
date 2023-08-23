from . import views
from django.urls import path
from taskapp.views import ctb_welcome, GuestCompletedList, MemberTodoList, create_task, FullTaskList


urlpatterns = [
    path('', views.ctb_welcome, name='member-home'),
    path('guest/', views.GuestCompletedList.as_view(), name='guest-completed-list'),
    path('create/', views.create_task, name='create-task'),
    path('full/', views.FullTaskList.as_view(), name='full-task-list'),
    path('todo/', views.get_todo_list, name='list'),
    ]
