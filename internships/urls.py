from django.urls import path
from . import views

urlpatterns = [
    path('', views.internship_list, name='internship_list'),
    path('post/', views.post_internship, name='post_internship'),
    path('<int:pk>/', views.internship_detail, name='internship_detail'),
    path('<int:pk>/apply/', views.apply_internship, name='apply_internship'),
]
