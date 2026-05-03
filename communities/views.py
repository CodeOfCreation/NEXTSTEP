from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Community, Membership, Message

from accounts.models import Activity

def explore_communities(request):
    communities = Community.objects.filter(is_public=True)
    user_memberships = []
    if request.user.is_authenticated:
        user_memberships = Membership.objects.filter(user=request.user).values_list('community_id', flat=True)
    return render(request, 'communities/explore.html', {
        'communities': communities,
        'user_memberships': user_memberships,
    })

def community_detail(request, pk):
    community = get_object_or_404(Community, pk=pk)
    is_member = False
    if request.user.is_authenticated:
        is_member = Membership.objects.filter(user=request.user, community=community).exists()
    members = community.members.all()[:10]
    messages_list = community.messages.select_related('sender').all()[:50]
    return render(request, 'communities/detail.html', {
        'community': community,
        'is_member': is_member,
        'members': members,
        'messages_list': messages_list,
    })


@login_required
def join_community(request, pk):
    community = get_object_or_404(Community, pk=pk)
    membership, created = Membership.objects.get_or_create(user=request.user, community=community)
    if created:
        Activity.objects.create(user=request.user, description=f'Joined community: {community.name}')
        messages.success(request, f'You have joined {community.name}!')
    else:
        messages.info(request, 'You are already a member.')
    return redirect('community_detail', pk=pk)

@login_required
def leave_community(request, pk):
    community = get_object_or_404(Community, pk=pk)
    Membership.objects.filter(user=request.user, community=community).delete()
    Activity.objects.create(user=request.user, description=f'Left community: {community.name}')
    messages.success(request, f'You have left {community.name}.')
    return redirect('community_detail', pk=pk)

@login_required
def create_community(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        topic_focus = request.POST.get('topic_focus', '')
        is_public = request.POST.get('is_public') == 'on'

        community = Community.objects.create(
            name=name,
            description=description,
            topic_focus=topic_focus,
            is_public=is_public,
            created_by=request.user
        )
        Membership.objects.create(user=request.user, community=community, role='admin')
        Activity.objects.create(user=request.user, description=f'Created community: {name}')
        messages.success(request, 'Community created successfully!')
        return redirect('community_detail', pk=community.pk)

    return render(request, 'communities/create.html')


@login_required
def post_message(request, pk):
    community = get_object_or_404(Community, pk=pk)
    if request.method == 'POST':
        if not Membership.objects.filter(user=request.user, community=community).exists():
            messages.error(request, 'You must be a member to post messages.')
            return redirect('community_detail', pk=pk)
        text = request.POST.get('text', '').strip()
        if text:
            Message.objects.create(community=community, sender=request.user, text=text)
    return redirect('community_detail', pk=pk)
