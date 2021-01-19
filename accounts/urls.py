from django.urls import path

from .views import registerPage

urlpatterns = [
    path('register/', registerPage, name='register'),
]