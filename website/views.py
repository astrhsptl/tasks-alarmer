from django.shortcuts import render,redirect
from django.views.generic import ListView
from django.contrib.auth import login, logout
from django.contrib.auth.models import User

from .forms import UserRegisterForm, UserAccountConfirmFormOrLogin
from .buisnes_logic.send_confirm_mail import send_confirm_email

class HomePage(ListView):
    template_name: str = 'pages/home.html'
    model = None

    def get(self, request) -> render:
        context = {
            'request': request,
        }
        return render(request, self.template_name, context)

class LoginPage(ListView):
    template_name: str = 'pages/login.html'
    model = None

    def post(self, request) -> redirect:
        form = UserAccountConfirmFormOrLogin(request.POST)
        if form.is_valid():
            try:
                take_user = User.objects.get(
                    email=form.data['email'],
                    password=form.data['password'],
                    )
                login(request, take_user)
            except Exception as e:
                return redirect('home')
        return redirect('home')

    def get(self, request) -> render:
        form = UserAccountConfirmFormOrLogin()
        context = {
            'form': form,
        }
        return render(request, self.template_name, context)
    
class RegisterPage(ListView):
    template_name: str = 'pages/register.html'
    model = None

    def post(self, request) -> redirect:
        form = UserRegisterForm(request.POST)
        if form.is_valid() and form.data['password'] == form.data['confirm_password']:
            try:
                if User.objects.get(email=form.data['email'], password=form.data['password']) is not None:
                    new_user = User(
                    username=form.data['username'], 
                    email=form.data['email'],
                    password=form.data['password'], 
                    is_active=False,
                    )
                    send_confirm_email(form.data['email'])
                    new_user.save()
            except Exception as e:
                print(f'some except: {e}')
        return redirect('home')

    def get(self, request) -> render:
        form = UserRegisterForm()
        context = {
            'form': form
        }
        return render(request, self.template_name, context)

class ConfirmPage(ListView):
    template_name: str = 'pages/confirm.html'
    model = None
    
    def post(self, request) -> redirect:
        form = UserAccountConfirmFormOrLogin(request.POST)
        if form.is_valid():
            user = User.objects.get(
            email=form.data['email'],
            password=form.data['password'],
            )
            print(user)
            user.is_active=True
            user.save()
            print(user.is_active)
        return redirect('home')

    def get(self, request) -> render:
        form = UserAccountConfirmFormOrLogin()
        context = {
            'form': form
        }
        return render(request, self.template_name, context)

def try_logouting(request) -> redirect:
    logout(request)
    return redirect('home')