from . import views
from django.urls import path


urlpatterns = [
    path('todo/', views.TodoTaskList.as_view(), name='todo-task-list'),
    path('completed/', views.CompletedTaskList.as_view(), name='completed-task-list'),
    # path('create/', views.CreateTask.as_view(), name='create-task'),
    # path('update/', views.UpdateTask.as_view(), name='update-task')
]
