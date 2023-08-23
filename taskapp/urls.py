from . import views
from django.urls import path
from taskapp.views import ctb_welcome, GuestCompletedList, MemberTodoList, create_task, FullTaskList


urlpatterns = [
    # path('todo/', views.TodoTaskList.as_view(), name='todo-task-list'),
    # path('', views.MemberTodoList.as_view(), name='member-todo-list'),
    path('guest/', views.GuestCompletedList.as_view(), name='guest-completed-list'),
    path('full/', views.FullTaskList.as_view(), name='full-task-list'),
    # path('', views.MemberTodoList.as_view(), name='member-todo-list'),
    path('create/', views.create_task, name='create-task'),
    # path('update/', views.UpdateTask.as_view(), name='update-task')
]
