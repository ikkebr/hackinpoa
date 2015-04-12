from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django import forms

def index(request):
    return render(request, 'base/index.html', {})


@login_required
def profile(request):
    return render(request, 'base/profile.html', {})

from users.models import UF_CHOICES, SEX_CHOICES, UserProfile

class ExtraUserCreationForm(UserCreationForm):
    nome = forms.CharField(max_length=50, required=True)
    cidade = forms.CharField(max_length=50, required=True)
    estado = forms.ChoiceField(choices=UF_CHOICES, required=True)
    sexo = forms.ChoiceField(choices=SEX_CHOICES, widget=forms.RadioSelect(), required=True)

def signup(request):
    if request.user.is_authenticated():
        return redirect(profile)

    form = ExtraUserCreationForm(request.POST or None)

    if form.is_valid():
        usuario = form.save()
        messages.success(request, 'Cadastro realizado com sucesso')
        profilex = UserProfile.objects.get(user=usuario)
        profilex.state = form.cleaned_data['estado']
        profilex.sex = form.cleaned_data['sexo']
        profilex.city = form.cleaned_data['cidade']
        profilex.name = form.cleaned_data['nome']
        profilex.save()


        return redirect(profile)

    return render(request, 'base/signup.html', {'form': form})
