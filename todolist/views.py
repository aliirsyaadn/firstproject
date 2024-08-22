from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def index(request):
    todos = Todo.objects.all()
    return render(request, 'index.html', {'todos': todos})

def add_todo(request):
    # Get data from the html form
    judul = request.POST['judul']
    description = request.POST['description']

    Todo.objects.create(title=judul, description=description)

    # notif email

    # integrasi ke payment

    return redirect('index')


def complete_todo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.completed = True
    todo.save()
    return redirect('index')

def delete_todo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.delete()
    return redirect('index')

def profile(request):
    return render(request, 'profile.html')

def data_json(request):
    todos = Todo.objects.all()

    return JsonResponse({
        'data': list(todos.values())
    })
    