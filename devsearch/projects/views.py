from pydoc import describe
from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
# Create your views here.
def projects(request):
    projects = Project.objects.all()
    contex = {'projects' : projects}
    return render(request, 'projects/projects.html', contex)


def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    return render(request, 'projects/single-project.html', {'project' : projectObj})
