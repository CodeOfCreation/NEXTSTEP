from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    BUDGET_CHOICES = [
        ('free', 'Free Resources Only'),
        ('mixed', 'Best Quality (Free + Paid)'),
    ]
    LEARNING_STYLE_CHOICES = [
        ('video', 'Video'),
        ('text', 'Text'),
        ('interactive', 'Interactive Labs'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    budget_mode = models.CharField(max_length=10, choices=BUDGET_CHOICES, default='mixed')
    learning_style = models.CharField(max_length=15, choices=LEARNING_STYLE_CHOICES, default='video')
    career_goal = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Activities'

    def __str__(self):
        return f"{self.user.username}: {self.description}"
