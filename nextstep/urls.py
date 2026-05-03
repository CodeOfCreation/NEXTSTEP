"""nextstep URL Configuration"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('roadmaps/', include('roadmaps.urls')),
    path('articles/', include('articles.urls')),
    path('internships/', include('internships.urls')),
    path('communities/', include('communities.urls')),
    path('dashboard/', include('dashboard.urls')),
]
