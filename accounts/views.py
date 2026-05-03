from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Profile, Activity

def home(request):
    return render(request, 'accounts/home.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        career_goal = request.POST.get('career_goal', '')
        budget_mode = request.POST.get('budget_mode', 'mixed')
        learning_style = request.POST.get('learning_style', 'video')

        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return redirect('signup')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists.')
            return redirect('signup')

        user = User.objects.create_user(username=username, email=email, password=password)
        Profile.objects.create(
            user=user,
            career_goal=career_goal,
            budget_mode=budget_mode,
            learning_style=learning_style
        )
        Activity.objects.create(user=user, description='Joined NEXTSTEP')
        messages.success(request, 'Account created successfully! Please log in.')
        return redirect('login')

    return render(request, 'accounts/signup.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            Activity.objects.create(user=user, description='Logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('login')
    return render(request, 'accounts/login.html')

def logout_view(request):
    if request.user.is_authenticated:
        Activity.objects.create(user=request.user, description='Logged out')
    logout(request)
    return redirect('home')

@login_required
def profile(request):
    profile, _ = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        profile.career_goal = request.POST.get('career_goal', '')
        profile.budget_mode = request.POST.get('budget_mode', 'mixed')
        profile.learning_style = request.POST.get('learning_style', 'video')
        profile.save()
        messages.success(request, 'Profile updated successfully!')
        return redirect('profile')
    return render(request, 'accounts/profile.html', {'profile': profile})
