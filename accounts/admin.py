from django.contrib import admin
from .models import Profile, Activity

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'career_goal', 'budget_mode', 'learning_style', 'created_at')
    list_filter = ('budget_mode', 'learning_style')

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('user', 'description', 'created_at')
    list_filter = ('created_at',)
