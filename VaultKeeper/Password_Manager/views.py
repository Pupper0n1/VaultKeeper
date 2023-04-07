from django.shortcuts import render, redirect, get_object_or_404
from .models import Password, User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from . import forms
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth.password_validation import validate_password
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.

def index_view(request):
    context = {}
    # return HttpResponse("HELLO")
    return render(request, "Password_Manager/index.html", context = context)

@login_required
def password_view(request):
    # print("ONE")
    if request.POST:
        form = forms.password_form(request.POST)
        # print("TWO")
        if form.is_valid():
            # print("THREE")
            link = form.cleaned_data['link']
            account = form.cleaned_data['account']
            password = form.cleaned_data['password']
            user = request.user
            Password.objects.create(website=link, username=account, password=password, user=user)
            return redirect(reverse('Password_Manager:passwords'))
    user = request.user.pk
    name = request.user.username
    passwords = Password.objects.filter(user=user)
    # print(passwords)
    # print("WTF")
    return render(request, "Password_Manager/passwords.html", context = {'passwords': passwords, 'user':name.capitalize(), 'password_form': forms.password_form, 'userID':user})


def about_view(request):
    return render(request, "Password_Manager/about.html")


# def login_view(request):
    # print("WHAAA")
    # if request.POST:
    #     username = request.POST.get('username').lower()
    #     password = request.POST.get('password')
    #     print(password)
    #     user = authenticate(request, username=username, password=password)

    #     if user is not None:
    #         login(request, user)
    #         return redirect(reverse('Password_Manager:passwords'))
    #     else:
    #         error_message = 'Invalid username or password!'
    #         return render(request, "registration/login.html", {'form':form, 'error':error_message})
    # else:
    #     form = forms.login_form()
    # return render(request, "registration/login.html", {'form':form})



def signup_view(request):
    if request.method == 'POST':
        form = forms.signup_form(request.POST)
        if form.is_valid():
            # validate password
            password = form.cleaned_data['password']
            try:
                validate_password(password)
            except Exception as e:
                # form.add_error('password', str(e))
                return render(request, 'registration/signup.html', {'form': form, 'errors': e})

            # create user
            username = form.cleaned_data['username'].lower()
            print(password)

            User.objects.create_user(username=username, password=password)
            user_auth = authenticate(request, username=username, password=password)
            if user_auth is not None:
                login(request, user_auth)
            return redirect(reverse('Password_Manager:passwords'))
    else:
        form = forms.signup_form()
    return render(request, "registration/signup.html", {'form': form})


def delete_view(request, pk):
    # print(userID)
    # for i in Password.objects.filter(user = User.objects.get(id=userID)):
    #     print(i.id)
    # print(request.user.username)
    # print(get_object_or_404(Password, pk=pk).user.username)
    print("START")
    print(f"pk is {pk}")
    try:
        password = Password.objects.filter(user=User.objects.get(id=request.user.id))[pk-2]
        print(password)
        if request.user.id == password.user.id:
            password.delete()
            return redirect(reverse('Password_Manager:passwords'))
        else:
            return HttpResponse("Do you not have permission to delete this password")
    except:
        return HttpResponse("Something went wrong!")
    

def logout_view(request):
    logout(request)
    # return render(request, 'Password_Manager/thankyou.html')


def thankyou_view(request):
    return render(request, 'Password_Manager/thankyou.html')



class CustomLoginView(LoginView):
    authentication_form = forms.CustomAuthenticationForm

