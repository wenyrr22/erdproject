from django.http import HttpResponse
from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from .forms import TaskForm
from .models import Task


from .models import Task


def hello(request):
    return render(request, 'index.html')

def today_tasks(request):
    today = timezone.now().date()
    tasks= Task.objects.filter(created_at__date=today)
    return render(request, 'today_tasks.html', {'today_tasks':tasks})
def all_task(request):
    tasks= Task.objects.all()
    return render(request, 'all_task.html', {'all_tasks':tasks})
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
           form.save()
           return redirect('task_added', title=form.cleaned_data['title'])
        else:
            form = TaskForm()
        return render(request, 'add_task.html', {'form': form})

def task_added(request, title):
    return render(request, 'task_added.html', {'title': title})

def edit_task(request, title):
    task = get_object_or_404(Task, title = title)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            updated_task = form.save(commit=False)
            updated_task.updated_at=timezone.now()
            updated_task.save()
            return redirect('task_update', title=form.cleaned_data['title'])
    else:
        form = TaskForm(instance=task)
    return render(request, 'edit_task.html', {'form': form})

def task_edited(request, title):
    return render(request, 'task_updated.html', {'title': title})

