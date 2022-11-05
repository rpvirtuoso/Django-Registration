from django.contrib import messages, auth
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.shortcuts import render, redirect
from django.urls import reverse

from users.forms import UserForm


# Create your views here.
def check_superuser(original_function):
    def wrapper_function(request):
        if request.user.is_authenticated:
            if request.user.is_superuser:
                messages.info(request, f"You are a super user")
            else:
                messages.error(request, f"You are not a superuser")
        return original_function(request)

    return wrapper_function


@check_superuser
def home(request):
    return render(request, 'home.html')


def signup(request):
    context = {}
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('login'))
    form = UserForm()
    context['form'] = form
    return render(request, 'signup.html', context)


def login_user(request):
    context = {}
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect(reverse('home'))
            else:
                messages.error(request, f"Invalid username or password")
                return redirect(reverse('login'))
        else:
            messages.error(request, "Invalid username or password.")
            return redirect(reverse('login'))
    form = AuthenticationForm()
    context['form'] = form
    return render(request, 'login.html', context)


def logout_user(request):
    auth.logout(request)
    return redirect(reverse('home'))


# def login_required(original_function):
#     def wrapper_function(request):
#         if request.user.is_authenticated:
#             pass
#         else:
#             messages.info(request, f"You need to log in first !")
#             redirect(reverse('home'))
#         return original_function(request)
#     return wrapper_function

def authenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated and request.session.get('user').get('is_authenticated'):
            return view_func(request, *args, **kwargs)
        else:
            return redirect('login')

    return wrapper_func


@authenticated_user
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, f"Password changed Successfully!")
            return redirect(reverse('login'))
        else:
            messages.error(request, 'Please correct the error below.')
    form = PasswordChangeForm(request.user)
    context = {'form': form}
    return render(request, 'password_change.html', context)
