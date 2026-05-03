from django.urls import path
from . import views

urlpatterns = [
    path('', views.explore_communities, name='explore_communities'),
    path('create/', views.create_community, name='create_community'),
    path('<int:pk>/', views.community_detail, name='community_detail'),
    path('<int:pk>/join/', views.join_community, name='join_community'),
    path('<int:pk>/leave/', views.leave_community, name='leave_community'),
    path('<int:pk>/message/', views.post_message, name='post_message'),
]
