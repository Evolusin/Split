"""Define URLs for /users/*"""

from django.urls import path, include
from . import views

app_name = 'users'

urlpatterns = [
    # Default auth urls
    path('', include('django.contrib.auth.urls')),
    # Password change
    path('upassword_change/', views.upassword_change, name='upassword_change'),
    # Get profile info
    path('profile/<int:profile_id>', views.profile, name='profile')
]