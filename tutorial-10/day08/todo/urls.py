from django.urls import path
from todo.views import home, all_tasks, add_task, edit_task, delete_task

urlpatterns = [
    path('', home, name='home'),
    path('all-tasks/', all_tasks, name='all_tasks'),
    path('add-task/', add_task, name='add_task'),
    path('edit-task/<int:task_id>/', edit_task, name='edit_task'),
    path('delete-task/<int:task_id>/', delete_task, name='delete_task'),
]