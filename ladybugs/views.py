from django.shortcuts import render
from django.contrib.auth import login, authenticate, get_user
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from ladybugs.models import Ingredients

# Create your views here.
from ladybugs.forms import SignUpForm


def main_page(request):
    return render(request, 'main.html',
                  {"name": get_user(request).get_username(), 'ingredients': Ingredients.objects.all()})


def register_page(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})


def login_page(request):
    return render(request, 'login.html', {})
