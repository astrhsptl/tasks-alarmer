from django import forms


class UserRegisterForm(forms.Form):
    username = forms.CharField(max_length=255, label='username')
    email = forms.CharField(max_length=255, label='email', widget=forms.EmailInput())
    password = forms.CharField(max_length=255, min_length=6, label='password', widget=forms.PasswordInput())
    confirm_password = forms.CharField(max_length=255, min_length=6, label='confirm password', widget=forms.PasswordInput())

class UserAccountConfirmFormOrLogin(forms.Form):
    email = forms.CharField(max_length=255, label='email', widget=forms.EmailInput())
    password = forms.CharField(max_length=255, min_length=6, label='password', widget=forms.PasswordInput())
