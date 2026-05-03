import io
import base64
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from roadmaps.models import Roadmap, Progress
from accounts.models import Activity, Profile
from communities.models import Community

@login_required
def dashboard(request):
    user = request.user
    profile, _ = Profile.objects.get_or_create(user=user)

    # Progress data
    progress_items = Progress.objects.filter(user=user, is_completed=True)
    total_topics = Progress.objects.filter(user=user).count()
    completed_count = progress_items.count()
    remaining_count = total_topics - completed_count

    # Generate chart
    chart_url = None
    if total_topics > 0:
        labels = ['Completed', 'Remaining']
        sizes = [completed_count, remaining_count]
        colors = ['#4CAF50', '#E0E0E0']

        fig, ax = plt.subplots(figsize=(6, 4))
        sns.set_style('whitegrid')
        ax.bar(labels, sizes, color=colors, edgecolor='black')
        ax.set_ylabel('Topics')
        ax.set_title('Your Learning Progress')
        for i, v in enumerate(sizes):
            ax.text(i, v + 0.5, str(v), ha='center', fontweight='bold')

        buf = io.BytesIO()
        plt.tight_layout()
        plt.savefig(buf, format='png')
        buf.seek(0)
        chart_url = base64.b64encode(buf.read()).decode('utf-8')
        plt.close()

    # Recent activities
    activities = Activity.objects.filter(user=user)[:10]

    # Communities
    user_communities = Community.objects.filter(members=user)[:5]

    # Active roadmaps
    active_roadmaps = Roadmap.objects.filter(
        topics__user_progress__user=user
    ).distinct()[:5]

    return render(request, 'dashboard/dashboard.html', {
        'profile': profile,
        'completed_count': completed_count,
        'remaining_count': remaining_count,
        'total_topics': total_topics,
        'chart_url': chart_url,
        'activities': activities,
        'user_communities': user_communities,
        'active_roadmaps': active_roadmaps,
    })
