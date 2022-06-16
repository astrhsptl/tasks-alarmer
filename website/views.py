from django.shortcuts import render,redirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth import login, logout
from django.contrib.auth.models import User

from website.models import Users_task
from .forms import UserRegisterForm, UserAccountConfirmFormOrLogin, CreateTaskForm
from .buisnes_logic.send_confirm_mail import send_confirm_email
from .buisnes_logic.interaction_with_db import create_new_user, get_concrete_user, confirming_user_account
from .buisnes_logic.interaction_with_db import add_task


def trying(request, slug='suka_blya'):
    return redirect('account', slug=slug)

class GetConcreteTask(DetailView):
    model = Users_task
    template_name: str = 'pages/task.html'

    def get(self, request, id):
        context = {
            'id': id
        }
        return render(request, self.template_name, context)

class CreateTask(ListView):
    model = None
    template_name = 'pages/create_task.html'

    def post(self, request) -> redirect:
        form  = CreateTaskForm(request.POST)
        users_id = request.user.pk
        if form.is_valid():
            try:
                new_task = add_task(form.data['title'], form.data['discription'], form.data['notification'], users_id)
            except:
                print('fuck u') 
        return redirect('home') 

    def get(self, request) -> render:
        form = CreateTaskForm()
        context = {
            'form': form,
        }
        return render(request, self.template_name, context)

class UserAccountDetailView(DetailView):
    model = User
    template_name = 'pages/datail_account.html'

    def get(self, request, slug):
        if request.user.username != slug:
            return redirect('home')
        context = self.get_context_data(slug)        
        return render(request, 'pages/datail_account.html', context)
    
    def get_context_data(self, slug) -> dict:
        get = User.objects.get(username=slug)
        query = User.objects.raw(f'''
        SELECT wut.status, wut.title, wut.id, bro.* 
        FROM website_users_task AS wut
        JOIN website_users_tasks_broker as bro
        ON bro.user_id_id={get.id}
        WHERE wut.status="compliting..." AND wut.id=bro.task_id_id;
        ''')
        context = {
            'query': query
        }
        return context

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
                #get_concrete_user
                take_user = get_concrete_user(
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
                    print(
                    form.data['username'], 
                    form.data['email'],
                    form.data['password'], 
                    )
                    new_user = create_new_user(
                    username=form.data['username'], 
                    email=form.data['email'],
                    password=form.data['password'], 
                    )
                    print(new_user)
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
            confirming_user_account(
            email=form.data['email'],
            password=form.data['password'],
            )
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
