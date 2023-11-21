from django.urls import path
from .views import goodbyeWorld
urlpatterns = [
    path('', goodbyeWorld, name='GoodbyeWorld')
]