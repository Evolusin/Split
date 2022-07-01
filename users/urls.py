"""Define URLs for /users/*"""

from django.urls import path, include
from . import views

app_name = 'users'

urlpatterns = [
    # Default auth urls
    path('', include('django.contrib.auth.urls')),
    # Login user
    # path('login/', views.login, name='login' ),
    # Password change
    path('upassword_change/', views.upassword_change, name='upassword_change'),

]