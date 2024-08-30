from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile, Link, Experience, Education, Testimony

class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'username', 'first_name', 'last_name', 'date_joined', 'last_login')
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user__username', 'created_at')
    readonly_fields = ('created_at',)


class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('client', 'start_year', 'end_year', 'created_at')
    readonly_fields = ('created_at',)
    prepopulated_fields = {"slug": ('client', )}


class EducationAdmin(admin.ModelAdmin):
    list_display = ('school', 'course', 'start_year', 'end_year', 'created_at')
    readonly_fields = ('created_at',)
    prepopulated_fields = {"slug": ('school', )}


class TestimonyAdmin(admin.ModelAdmin):
    list_display = ('writer', 'created_at')
    readonly_fields = ('created_at',)



admin.site.register(User, CustomUserAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Link)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Testimony, TestimonyAdmin)

