from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from .models import User, Profile, Experience, Testimony
from django.core.mail import send_mail
from portfolio.settings import EMAIL_HOST_USER
from django.http import FileResponse, Http404
import os
from django.conf import settings


def base_view(request):
    user = User.objects.all().first()
    return render(request, 'user/base.html', context={'user': user})


def profile(request):
    user = User.objects.all().first()
    profile = Profile.objects.all().first()
    return render(request, 'user/profile.html', context={'user': user, 'profile': profile})


def experience(request):
    user = User.objects.all().first()
    experiences = Experience.objects.all()
    return render(request, 'user/experiences.html', context={'experiences': experiences, 'user': user})


def create_testimony(request):
    if request.method == "POST":
        testimony = Testimony.objects.create(
            profile = Profile.objects.all().first(),
            writer = request.POST.get('writer'),
            image = request.FILES.get('image'),
            occupation = request.POST.get('occupation'),
            company = request.POST.get('company'),
            text = request.POST.get('text')
        )
        testimony.save()
        messages.success(request, "your testimonial has been added")
        return HttpResponseRedirect(reverse('testimonies'))
    else:
        user = User.objects.all().first()
        return render(request, 'user/create_testimony.html', context={'user': user})


def testimony(request):
    user = User.objects.all().first()
    testimonies = Testimony.objects.all()
    return render(request, 'user/testimonies.html', context={'testimonies': testimonies, 'user': user})


def contact_me(request):
    user = User.objects.all().first()
    if request.method == "POST":
        name = request.POST.get('writer')
        email = request.POST.get('email')
        form_message = request.POST.get('text')

        subject = f"{name} needs your service!"
        message =  f"message from {email}: {form_message}"
        recipient_list = ['oladotunkolapo@gmail.com']
        send_mail(subject, message, EMAIL_HOST_USER, recipient_list, fail_silently=False)
        messages.success(request, "your message has been sent")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return render(request, 'user/contact.html', context={'user': user})
    

def download_resume(request, file_name):
    path_to_file = os.path.join(settings.MEDIA_ROOT, file_name)

    if os.path.exists(path_to_file):
        response = FileResponse(open(path_to_file, 'rb'))
        response['Content-Disposition'] = f'attachment; filename="{file_name}"'
        return response
    else:
        return Http404('file not found')

