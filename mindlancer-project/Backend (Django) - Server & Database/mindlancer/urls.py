from django.contrib import admin
from django.urls import path, include
from .views import home  # Import the home view


urlpatterns = [
    path('', home, name='home'),  # Add this line for the home view

    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    path('api/jobs/', include('jobs.urls')),
    path('api/proposals/', include('proposals.urls')),
]
