from django.urls import path, include

urlpatterns = [
    path('tweets', include('tweets.urls')),
    path('account', include('account.urls')),
]
