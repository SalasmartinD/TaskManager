from django.urls import path
from .views import list_tasks, create_task, delete_tasks

urlpatterns = [
    path('', list_tasks),
    path('delete/<int:task_id>/', delete_tasks, name='delete_task'),
    path('new/', create_task, name='create_task'),
]