from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Project
from .models import Todolist
# Create your views here.
@login_required(login_url="/login/")
def add(request, project_id):
    project = Project.objects.filter(created_by=request.user).get(pk=project_id)
    if request.method == 'POST':
        name = request.POST.get('name' '')
        description = request.POST.get('description' '')

        if name:
            Todolist.objects.create(name=name, description=description, project=project, created_by=request.user)
            return redirect(f'/projects/{project_id}/')
    return render(request, 'todolist/add.html', {'project': project})

@login_required(login_url="/login/")
def todolist(request, project_id, pk):
    project = Project.objects.filter(created_by=request.user).get(pk=project_id)
    todolist = Todolist.objects.filter(project=project).get(pk=pk)
    tasks_ = todolist.tasks.all()
    completed_task = tasks_.filter(is_done=True)

    return render(request, 'todolist/todolist.html', {'project': project, 'todolist': todolist, 'completed_task': completed_task})

@login_required(login_url="/login/")
def edit(request, project_id, pk):
    project = Project.objects.filter(created_by=request.user).get(pk=project_id)
    todolist = Todolist.objects.filter(project=project).get(pk=pk)

    if request.method == 'POST':
        name = request.POST.get('name' '')
        description = request.POST.get('description' '')
       
        if name:
            todolist.name = name
            todolist.description = description
            todolist.save()
            print(todolist)
            return redirect(f'/projects/{project_id}/{pk}/')
           
    return render(request, 'todolist/edit.html', {'project': project, 'todolist': todolist})

@login_required(login_url="/login/")
def delete(request, project_id, pk):
    project = Project.objects.filter(created_by=request.user).get(pk=project_id)
    todolist = Todolist.objects.filter(project=project).get(pk=pk)

    todolist.delete()

    return redirect(f'/projects/{project_id}/')

