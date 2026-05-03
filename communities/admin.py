from django.contrib import admin
from .models import Community, Membership

class MembershipInline(admin.TabularInline):
    model = Membership
    extra = 1

@admin.register(Community)
class CommunityAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_by', 'member_count', 'created_at', 'is_public')
    list_filter = ('is_public', 'created_at')
    search_fields = ('name', 'description', 'topic_focus')
    inlines = [MembershipInline]

@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    list_display = ('user', 'community', 'role', 'joined_at')
    list_filter = ('role',)
