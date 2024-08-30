from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse
from .models import User, Profile, Experience, Education, Testimony


def base_view(request):
    user = User.objects.all().first()
    return render(request, 'user/base.html', context={'user': user})


def profile(request):
    user = User.objects.all().first()
    profile = Profile.objects.all().first()
    return render(request, 'user/profile.html', context={'user': user, 'profile': profile})


def experience(request):
    experiences = Experience.objects.all()
    return render(request, 'user/experiences.html', context={'experiences': experiences})


def education(request):
    education_history = Education.objects.all()
    return render(request, 'user/education.html', context={'education_history': education_history})


def create_testimony(request):
    if request.method == "POST":
        testimony = Testimony.objects.create(
            profile = Profile.objects.all().first(),
            writer = request.POST.get('writer'),
            occupation = request.POST.get('occupation'),
            company = request.POST.get('company'),
            text = request.POST.get('text')
        )
        testimony.save()
        return HttpResponseRedirect(reverse('testimonies'))
    else:
        return render(request, 'user/create_testimony.html', context={})


def testimony(request):
    testimonies = Testimony.objects.all()
    return render(request, 'user/testimonies.html', context={'testimonies': testimonies})