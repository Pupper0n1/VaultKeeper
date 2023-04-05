from django import forms
from django.contrib.auth.forms import AuthenticationForm


# class login_form(forms.Form):
#     username = forms.CharField(label='Username', max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
#     password = forms.CharField(label='Password', max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))



class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label='Username', max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', max_length=255, widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class signup_form(forms.Form):
    username = forms.CharField(label='Username', max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', max_length=255, widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class password_form(forms.Form):
    link = forms.URLField(label='Link', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'www.example.com'}))
    account = forms.CharField(label='Account', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'example@email.com'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '**********'}))
