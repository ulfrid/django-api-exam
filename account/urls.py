from django.urls import path
from .views      import SignUpView, AuthView, UserView
urlpatterns = [
    path('/sign-up', SignUpView.as_view()),
    path('/sign-in', AuthView.as_view()),
    path('', UserView.as_view()),
]
