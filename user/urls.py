from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('experience/', views.experience, name='experience'),
    path('create-testimonial/', views.create_testimony, name='create-testimonial'),
    path('testimonials/', views.testimony, name='testimonials'),
    path('contact-me/', views.contact_me, name='contact-me'),
    path('download/<str:file_name>', views.download_resume, name='download-resume')

]