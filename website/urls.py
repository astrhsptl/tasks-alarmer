from django.urls import path

from .views import HomePage, LoginPage


urlpatterns = [
    path('', HomePage.as_view()),
    path('login/', LoginPage.as_view())
]
