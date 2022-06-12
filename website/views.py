from django.shortcuts import render
from django.views.generic import ListView


class HomePage(ListView):
    template_name: str = 'base.html'
    model = None

    def get(self, request) -> render:
        context = {
            'some': 'home',
        }
        return render(request, 'pages/home.html', context)

class LoginPage(ListView):
    template_name: str = 'base.html'
    model = None

    def get(self, request) -> render:
        context = {
            'some': 'login',
        }
        return render(request, 'pages/login.html', context)