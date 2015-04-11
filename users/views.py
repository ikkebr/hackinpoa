from django.shortcuts import render
from django import forms
from .models import UserProfile
from django.contrib import messages
from django.contrib.auth.decorators import login_required


class PerfilForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ['name', 'sex', 'city', 'state', 'motorcycle', 'cc', 'year', 'category', 'manufactured']

@login_required
def edit_profile(request):
	#print dir(request.user)
	#print "oi"
	#print request.user.userprofile
	form = PerfilForm(request.POST or None, instance=request.user.userprofile)

	if form.is_valid():
		f = form.save(commit = False)
		f.user = request.user
		f.save()
		messages.success(request, 'Perfil atualizado com sucesso.')
		return redirect('profile')

	return render(request, "account/edit.html", { 'form': form })