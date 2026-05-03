from django.db import models
from django.contrib.auth.models import User

class Roadmap(models.Model):
    DIFFICULTY_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    career_role = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES, default='beginner')
    estimated_duration = models.CharField(max_length=50, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_roadmaps')

    created_at = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def total_topics(self):
        return self.topics.count()

    class Meta:
        ordering = ['-created_at']

class Topic(models.Model):
    roadmap = models.ForeignKey(Roadmap, on_delete=models.CASCADE, related_name='topics')
    title = models.CharField(max_length=200)
    description = models.TextField()
    estimated_time = models.CharField(max_length=50)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.roadmap.title} - {self.title}"

    class Meta:
        ordering = ['order']

class Resource(models.Model):
    RESOURCE_TYPE_CHOICES = [
        ('free', 'Free'),
        ('paid', 'Paid'),
    ]
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='resources')
    title = models.CharField(max_length=200)
    url = models.URLField()
    resource_type = models.CharField(max_length=10, choices=RESOURCE_TYPE_CHOICES, default='free')
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Progress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='roadmap_progress')
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='user_progress')
    is_completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        status = "Completed" if self.is_completed else "In Progress"
        return f"{self.user.username} - {self.topic.title} ({status})"

    class Meta:
        unique_together = ('user', 'topic')
        verbose_name_plural = 'Progress Entries'
