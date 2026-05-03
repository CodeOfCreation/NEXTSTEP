from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Internship, Application
from accounts.models import Activity

def internship_list(request):
    internships = Internship.objects.filter(is_active=True)
    return render(request, 'internships/list.html', {'internships': internships})

def internship_detail(request, pk):
    internship = get_object_or_404(Internship, pk=pk, is_active=True)
    has_applied = False
    if request.user.is_authenticated:
        has_applied = Application.objects.filter(internship=internship, applicant=request.user).exists()
    return render(request, 'internships/detail.html', {
        'internship': internship,
        'has_applied': has_applied,
    })

@login_required
def apply_internship(request, pk):
    internship = get_object_or_404(Internship, pk=pk, is_active=True)
    if Application.objects.filter(internship=internship, applicant=request.user).exists():
        messages.info(request, 'You have already applied for this internship.')
        return redirect('internship_detail', pk=pk)

    if request.method == 'POST':
        cover_letter = request.POST.get('cover_letter', '')
        Application.objects.create(
            internship=internship,
            applicant=request.user,
            cover_letter=cover_letter
        )
        Activity.objects.create(user=request.user, description=f'Applied to internship: {internship.title}')
        messages.success(request, 'Application submitted successfully!')
        return redirect('internship_detail', pk=pk)

    return render(request, 'internships/apply.html', {'internship': internship})

@login_required
def post_internship(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        company = request.POST.get('company')
        description = request.POST.get('description')
        location = request.POST.get('location', '')
        is_remote = request.POST.get('is_remote') == 'on'
        deadline = request.POST.get('deadline') or None

        internship = Internship.objects.create(
            title=title,
            company=company,
            description=description,
            location=location,
            is_remote=is_remote,
            posted_by=request.user,
            deadline=deadline
        )
        Activity.objects.create(user=request.user, description=f'Posted internship: {title}')
        messages.success(request, 'Internship posted successfully!')
        return redirect('internship_detail', pk=internship.pk)

    return render(request, 'internships/post.html')
