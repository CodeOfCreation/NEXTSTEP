from django.urls import path
from . import views

urlpatterns = [
    path('', views.explore, name='roadmap_explore'),
    path('create/', views.create_roadmap, name='roadmap_create'),
    path('<int:pk>/', views.detail, name='roadmap_detail'),
    path('topic/<int:topic_id>/complete/', views.mark_complete, name='mark_complete'),
]
