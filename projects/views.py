from django.shortcuts import render, get_object_or_404
from projects.models import Project
from django.contrib.auth.decorators import login_required


# PROJECT LIST


@login_required
def list_projects(request):
    projects = Project.objects.filter(owner=request.user)
    context = {
        "projects": projects,
    }
    return render(request, "projects/list.html", context)


@login_required
def show_project(request, id):
    details = get_object_or_404(Project, id=id)
    context = {
        "details": details,
    }
    return render(request, "projects/details.html", context)
