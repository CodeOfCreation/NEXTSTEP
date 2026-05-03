from django.db import models
from django.contrib.auth.models import User

class Community(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_communities')
    created_at = models.DateTimeField(auto_now_add=True)
    members = models.ManyToManyField(User, through='Membership', related_name='communities')
    topic_focus = models.CharField(max_length=100, blank=True)
    is_public = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def member_count(self):
        return self.members.count()

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Communities'

class Membership(models.Model):
    ROLE_CHOICES = [
        ('member', 'Member'),
        ('admin', 'Admin'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    community = models.ForeignKey(Community, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='member')
    joined_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} in {self.community.name}"

    class Meta:
        unique_together = ('user', 'community')


class Message(models.Model):
    community = models.ForeignKey(Community, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='community_messages')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender.username}: {self.text[:30]}"

    class Meta:
        ordering = ['-created_at']
