from . import views
from django.urls import path
from taskapp import views


urlpatterns = [
    path('', views.ctb_welcome, name='member-home'),
    path('guest/', views.GuestCompletedList.as_view(), name='guest-completed-list'),
    path('create/', views.create_task, name='create-task'),
    path('edit/<task_id>', views.edit_task, name='edit'),
    path('delete/<task_id>', views.delete_task, name='delete'),
    path('full/', views.FullTaskList.as_view(), name='full-task-list'),
    path('todo/', views.get_todo_list, name='list'),
    ]
