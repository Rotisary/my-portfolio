from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.conf import settings
from django.template.defaultfilters import slugify
from django.db.models.signals import post_save
from django.dispatch import receiver
from cloudinary.models import CloudinaryField


class UserManager(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, password=None):
        if not email:
            raise ValueError("users must have an email address")
        if not username:
            raise ValueError("users must have a username")
        if not first_name:
            raise ValueError("users must enter a first_name")
        if not last_name:
            raise ValueError("users must enter a last_name")
        

        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
        

    def create_superuser(self, email, username, first_name, last_name, password):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
            first_name = first_name,
            last_name = last_name,
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(max_length=100, verbose_name='email', unique=True, null=False)
    username = models.CharField(max_length=30, unique=True, null=False)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True, null=False)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True, null=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    phone_number = models.CharField(max_length=11, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    objects = UserManager()


    def __str__(self):
        return f"{self.username}"
    

    def has_perm(self, perm, obj=None):
        return self.is_admin
    

    def has_module_perms(self, app_label):
        return True


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, null=False, on_delete=models.CASCADE)
    about = models.TextField(blank=True)
    image = CloudinaryField('image', use_filename=True, unique_filename=False, folder='portfolio_profile_pics')
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    slug = models.SlugField(blank=True, unique=True)


    def save(self, *args, **kwargs):
        first_name = self.user.first_name
        last_name = self.user.last_name
        full_name = f"{first_name} {last_name} {self.id}"
        self.slug = slugify(full_name)
        return super().save(*args, **kwargs)


    def __str__(self):
        return f"{self.user.username}'s profile"
    

class Experience(models.Model):
    profile = models.ForeignKey(Profile, related_name='experience', on_delete=models.CASCADE)
    details = models.TextField(blank=False)
    client = models.CharField(max_length=100, verbose_name='client/organisation', blank=False)
    start_year = models.DateField(null=False, blank=False)
    end_year = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    slug = models.SlugField(blank=False, unique=True)


    def __str__(self):
        return f"{self.client}"
    

class Testimony(models.Model):
    profile = models.ForeignKey(Profile, related_name='testimonies', on_delete=models.CASCADE)
    writer = models.CharField(max_length=100, verbose_name='name', blank=False)
    image = image = CloudinaryField('image', use_filename=True, unique_filename=False, folder='testimony_writer_images')
    occupation = models.CharField(max_length=100, blank=False)
    company = models.CharField(max_length=100, blank=True)
    text = models.TextField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False) 


    def __str__(self):
        return f"{self.writer}-{self.id}"