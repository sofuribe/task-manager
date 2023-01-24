from django.shortcuts import render, redirect
from tasks.forms import TaskForm
from django.contrib.auth.decorators import login_required
from tasks.models import Task


@login_required
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            task.save()
            return redirect("list_projects")
    else:
        form = TaskForm()

    context = {
        "form": form,
    }
    return render(request, "tasks/create.html", context)


@login_required
def show_my_tasks(request):
    my_tasks = Task.objects.filter(assignee=request.user)
    context = {
        "my_tasks": my_tasks,
    }
    return render(request, "tasks/mine.html", context)
