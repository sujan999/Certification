from django.shortcuts import render
from .models import Todo
# Create your views here.


def index(request):
    todo_list = Todo.objects.all()
    context = {
        "todo_list": todo_list,
        "home": True
    }
    return render(request, 'home/index.html', context)


def completed(request):
    completed_list = Todo.objects.filter(status='com')
    context = {
        "todo": completed_list,
        "completed": True
    }
    return render(request, 'home/completed.html', context)


def pending(request):
    pending_list = Todo.objects.filter(status='pen')
    context = {
        "todos": pending_list,
        "pending": True
    }
    return render(request, 'home/pending.html', context)
