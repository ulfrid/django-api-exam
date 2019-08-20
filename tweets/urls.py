from django.urls import path
from .views import *

urlpatterns = [
    path('', Tweet.as_view()),
]
