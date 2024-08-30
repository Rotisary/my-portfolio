from django.db import models
from django.conf import settings


class Skill(models.Model):
    name = models.CharField(max_length=100, blank=False)
    field = models.CharField(max_length=100, blank=False)
    expertise = models.IntegerField(default=1, null=True)
    added_at = models.DateTimeField(auto_now_add=True, null=False)
    slug = models.SlugField(blank=False, unique=True)


    def __str__(self):
        return f'{self.name}'


class ProjectManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_solo=True)
    


class Project(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='projects', null=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=False, unique=True)
    industry = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=False)
    skills_used = models.ManyToManyField(Skill, related_name='projects')
    website_link = models.URLField(verbose_name='website', blank=True, unique=True)
    github_link = models.URLField(verbose_name='github', blank=False, unique=True)
    is_solo = models.BooleanField(default=True)
    added_at = models.DateTimeField(auto_now_add=True, null=False)
    slug = models.SlugField(blank=False, unique=True)

    objects = models.Manager()
    solo = ProjectManager()


    def __str__(self):
        return f'{self.name}'

