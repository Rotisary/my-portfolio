from django.shortcuts import render
from .models import Skill, Project
from user.models import User


def skills(request):
    user = User.objects.all().first()
    skills = Skill.objects.all()
    return render(request, 'project/skills.html', context={'skills': skills, 'user': user})


def projects(request):
    user = User.objects.all().first()
    projects = Project.objects.all()
    return render(request, 'project/projects.html', context={'projects': projects, 'user': user})
