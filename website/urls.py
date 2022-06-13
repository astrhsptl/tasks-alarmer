from django.urls import path

from .views import HomePage, LoginPage, RegisterPage
from .views import ConfirmPage, try_logouting


urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('login/', LoginPage.as_view(), name='login'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('confirm/', ConfirmPage.as_view()),
    path('logout/', try_logouting, name='logout'),
    #path('account/<int:pk>', , name='account'),

]
