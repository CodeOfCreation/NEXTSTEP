from django.contrib import admin
from .models import Internship, Application

@admin.register(Internship)
class InternshipAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'posted_by', 'created_at', 'is_active', 'deadline')
    list_filter = ('is_active', 'is_remote', 'created_at')
    search_fields = ('title', 'company', 'description')

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('internship', 'applicant', 'status', 'applied_at')
    list_filter = ('status', 'applied_at')
