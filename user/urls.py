from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    # path('profile/', views.profile, name='profile'),
    path('experience/', views.experience, name='experience'),
    path('education/', views.education, name='education'),
    path('create-testimony/', views.create_testimony, name='create-testimony'),
    path('testimony/', views.testimony, name='testimonies'),

]