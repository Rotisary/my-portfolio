from django.contrib import admin
from .models import Project, Skill


class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'field', 'added_at')
    search_fields = ('name','field')
    readonly_fields = ('added_at',)
    prepopulated_fields = {'slug': ('name',)}


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'industry', 'website_link', 'added_at')
    search_fields = ('name','user__first_name', 'user__last_name', 'industry')
    readonly_fields = ('added_at',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Skill, SkillAdmin)
admin.site.register(Project, ProjectAdmin)
