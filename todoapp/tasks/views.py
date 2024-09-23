from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Task


def index(request):
    tasks = Task.objects.all().order_by('-created_at')
    context = {'tasks': tasks}
    return render(request, 'tasks/index.html', context)


def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        category = request.POST.get('category')
        task = Task(title=title, description=description, category=category)
        task.save()
        return redirect('tasks:index')
    return render(request, 'tasks/add_task.html')


def update_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.category = request.POST.get('category')
        task.completed = 'completed' in request.POST
        task.save()
        return redirect('tasks:index')
    context = {'task': task}
    return render(request, 'tasks/update_task.html', context)


def delete_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.delete()
    return redirect('tasks:index')


def complete_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.completed = not task.completed
    task.save()
    return HttpResponseRedirect(reverse('tasks:index'))
