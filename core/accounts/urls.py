from django.urls import path
from .views import *
from django.conf.urls.static import static

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register'),


]