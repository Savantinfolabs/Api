from django.urls import path, include
from rest_framework.authtoken import views
from .views import Amount


urlpatterns = [
    path('', Amount),
]