from django.urls import path, include

urlpatterns = [
    path('tweets', include('tweets.urls')),
]
