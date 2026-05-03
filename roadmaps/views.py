from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from .models import Roadmap, Topic, Resource, Progress
from accounts.models import Activity
from django.utils import timezone

def explore(request):
    roadmaps = Roadmap.objects.filter(is_public=True)
    return render(request, 'roadmaps/explore.html', {'roadmaps': roadmaps})

def detail(request, pk):
    roadmap = get_object_or_404(Roadmap, pk=pk)
    topics = list(roadmap.topics.prefetch_related('resources'))
    progress_dict = {}
    next_topic = None
    if request.user.is_authenticated:
        progress_qs = Progress.objects.filter(user=request.user, topic__roadmap=roadmap)
        progress_dict = {p.topic_id: p.is_completed for p in progress_qs}
        for topic in topics:
            if not progress_dict.get(topic.id, False):
                next_topic = topic
                break
    for topic in topics:
        topic.is_completed = progress_dict.get(topic.id, False)
        topic.is_next = (topic == next_topic)
    return render(request, 'roadmaps/detail.html', {
        'roadmap': roadmap,
        'topics': topics,
    })


@login_required
def create_roadmap(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        career_role = request.POST.get('career_role')
        difficulty = request.POST.get('difficulty', 'beginner')
        estimated_duration = request.POST.get('estimated_duration', '')
        roadmap = Roadmap.objects.create(
            title=title,
            description=description,
            career_role=career_role,
            difficulty=difficulty,
            estimated_duration=estimated_duration,
            created_by=request.user
        )
        
        # Parse dynamic topics
        topic_idx = 0
        while True:
            topic_title = request.POST.get(f'topic_title_{topic_idx}')
            if not topic_title:
                break
            topic = Topic.objects.create(
                roadmap=roadmap,
                title=topic_title,
                description=request.POST.get(f'topic_description_{topic_idx}', ''),
                estimated_time=request.POST.get(f'topic_estimated_time_{topic_idx}', ''),
                order=topic_idx
            )
            
            # Parse resources for this topic
            resource_idx = 0
            while True:
                resource_title = request.POST.get(f'resource_title_{topic_idx}_{resource_idx}')
                if not resource_title:
                    break
                Resource.objects.create(
                    topic=topic,
                    title=resource_title,
                    url=request.POST.get(f'resource_url_{topic_idx}_{resource_idx}', ''),
                    resource_type=request.POST.get(f'resource_type_{topic_idx}_{resource_idx}', 'free')
                )
                resource_idx += 1
            
            topic_idx += 1
        
        Activity.objects.create(user=request.user, description=f'Created roadmap: {title}')
        messages.success(request, 'Roadmap created successfully!')
        return redirect('roadmap_detail', pk=roadmap.pk)
    return render(request, 'roadmaps/create.html')



@login_required
def mark_complete(request, topic_id):
    if request.method == 'POST':
        topic = get_object_or_404(Topic, pk=topic_id)
        progress, created = Progress.objects.get_or_create(user=request.user, topic=topic)
        progress.is_completed = True
        progress.completed_at = timezone.now()
        progress.save()
        Activity.objects.create(user=request.user, description=f'Completed topic: {topic.title}')
        messages.success(request, 'Topic marked as complete!')
        return redirect('roadmap_detail', pk=topic.roadmap.pk)
    messages.error(request, 'Invalid request.')
    return redirect('roadmap_explore')
