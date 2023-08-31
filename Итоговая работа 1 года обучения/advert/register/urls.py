from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import *



urlpatterns = [
    path('login', login_view, name='login'),
    path('logout', logout_view, name='logout'),
    path('profile', profile_view, name='profile'),
    path('register', registration_view, name='register'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
