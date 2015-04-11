from django.shortcuts import render
from django import forms
from .models import UserProfile
from django.contrib import messages

class PerfilForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ['name', 'sex', 'city', 'state', 'motorcycle', 'cc', 'year', 'category', 'manufactured']


def edit_profile(request):
	form = PerfilForm(request.POST or None, instance=request.user.userprofile)

	if form.is_valid():
		f = form.save(commit = False)
		f.user = request.user
		f.save()
		messages.success('Perfil atualizado com sucesso.')

	return render(request, "users/edit.html", { 'form': form })