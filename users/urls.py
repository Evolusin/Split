"""Define URLs for /users/*"""

from django.urls import path, include
from . import views

app_name = 'users'

urlpatterns = [
    # Default auth urls
    path('', include('django.contrib.auth.urls')),
    # Registration page
    path('register/', views.register, name='register'),
    # Password change
    path('upassword_change/', views.upassword_change, name='upassword_change'),

]