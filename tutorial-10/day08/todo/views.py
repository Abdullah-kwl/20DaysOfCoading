from django.shortcuts import redirect, render, get_object_or_404
from todo.models import TodoTask
from todo.forms import TodoTaskForm

# Create your views here.
def home(request):
    return render(request, 'todo/home.html')

def all_tasks(request):
    tasks = TodoTask.objects.all()
    return render(request, 'todo/all_tasks.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        form = TodoTaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_tasks')
    else:
        form = TodoTaskForm()
    return render(request, 'todo/add_task.html', {'form': form})

def edit_task(request, task_id):
    task = TodoTask.objects.get(id=task_id)
    if request.method == 'POST':
        form = TodoTaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('all_tasks')
    else:
        form = TodoTaskForm(instance=task)
    return render(request, 'todo/edit_task.html', {'form': form, 'task': task})

def delete_task(request, task_id):
    task = TodoTask.objects.get(id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('all_tasks')
