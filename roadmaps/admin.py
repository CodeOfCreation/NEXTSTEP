from django.contrib import admin
from .models import Roadmap, Topic, Resource, Progress

class ResourceInline(admin.TabularInline):
    model = Resource
    extra = 1

class TopicInline(admin.TabularInline):
    model = Topic
    extra = 1

@admin.register(Roadmap)
class RoadmapAdmin(admin.ModelAdmin):
    list_display = ('title', 'career_role', 'created_by', 'created_at', 'is_public')
    list_filter = ('is_public', 'created_at')
    search_fields = ('title', 'career_role')
    inlines = [TopicInline]

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'roadmap', 'estimated_time', 'order')
    list_filter = ('roadmap',)
    inlines = [ResourceInline]

@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'topic', 'resource_type', 'is_verified', 'url')
    list_filter = ('resource_type', 'is_verified')

@admin.register(Progress)
class ProgressAdmin(admin.ModelAdmin):
    list_display = ('user', 'topic', 'is_completed', 'completed_at')
    list_filter = ('is_completed',)
