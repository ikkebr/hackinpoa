from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def index(request):
    return render(request, 'base/index.html', {})


@login_required
def profile(request):
    return render(request, 'base/profile.html', {})


def signup(request):
    if request.user.is_authenticated():
        return redirect(profile)

    form = UserCreationForm(request.POST or None)

    if form.is_valid():
        usuario = form.save()
        messages.success(request, 'Cadastro realizado com sucesso')
        return redirect(profile)

    return render(request, 'base/signup.html', {'form': form})
