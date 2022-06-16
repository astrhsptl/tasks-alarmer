from django.urls import path

from .views import HomePage, LoginPage, RegisterPage
from .views import ConfirmPage, try_logouting, trying
from .views import UserAccountDetailView, CreateTask
from .views import GetConcreteTask


urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('login/', LoginPage.as_view(), name='login'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('confirm/', ConfirmPage.as_view()),
    path('logout/', try_logouting, name='logout'),
    path('account/<str:slug>', UserAccountDetailView.as_view(), name='account'),
    path('createtask/', CreateTask.as_view(), name='createtask'),
    path('conctretetask/<int:id>', GetConcreteTask.as_view(), name='task'),
]
