#encoding: utf-8
import datetime

from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, DetailView, TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import Http404, HttpResponse
from django.contrib.auth import logout
from django import forms

from .models import Group, Group_Access

from django.contrib import messages


class GroupCreateForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'is_public']

def logout_view(request):
    logout(request)
    return redirect('django.contrib.auth.views.login')


class LoginRequiredMixin(object):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)


class GroupCreate(LoginRequiredMixin, TemplateView):
    def get(self, request):
        form = GroupCreateForm()
        return render(request, "groups/group_create.html", {'form': form})

    def post(self, request):
        form = GroupCreateForm(request.POST or None)

        if form.is_valid():
            grupo = form.save(commit=False)
            grupo.owner = request.user
            grupo.save()

            messages.success(request, 'Grupo criado com sucesso')

        return redirect(grupo)


class GroupList(LoginRequiredMixin, ListView):
    model = Group

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Group.objects.all()

        return Group.objects.filter(id__in=[each.group.id for each in Group_Access.objects.filter(user=self.request.user)])

    def get_context_data(self, **kwargs):
        context = super(GroupList, self).get_context_data(**kwargs)
        context['public_groups'] = Group.objects.filter(is_public=True)

        return context

class GroupDetail(LoginRequiredMixin, DetailView):
    model = Group

    def get_queryset(self):
        self.group = get_object_or_404(Group, id=self.kwargs['pk'])

        #if not self.request.user.is_superuser:
        #    self.access = get_object_or_404(Group_Access, group=self.group, user=self.request.user)

        #if self.request.user.is_superuser or self.access:

        return Group.objects.filter(id=self.group.id)

        #raise Http404(u"Acesso negado a esse grupo.")

    def get_context_data(self, **kwargs):
        context = super(GroupDetail, self).get_context_data(**kwargs)
        context['grupo'] = self.group
        context['query'] = self.request.GET.get('q', '')
        context['currpage'] = 'isall'
        context['is_member'] = Group_Access.objects.filter(group=self.group, user=self.request.user)
        return context



class GroupAddMember(forms.ModelForm):
    class Meta:
        model = Group_Access
        fields = ['user', 'is_admin']


@login_required
def join_group(request, pk):
    group = get_object_or_404(Group, id=pk)
    access, created = Group_Access.objects.get_or_create(group=group, user=request.user)
    access.save()

    if created:
        messages.success(request, 'Você entrou no grupo.')

    return redirect(group)

def leave_group(request, pk):
    group = get_object_or_404(Group, id=pk)
    access, created = Group_Access.objects.get_or_create(group=group, user=request.user)

    if access.is_admin:
        messages.warning(request, 'Você não pode sair do grupo.')
        return redirect(group)

    access.delete()

    messages.success(request, 'Você saiu do grupo.')
    return redirect(group)


@login_required
def add_group_members(request, pk):
    group = get_object_or_404(Group, id=pk)
    if not request.user.is_superuser:
        access = get_object_or_404(Group_Access, group=group, user=request.user, is_admin=True)

    
    from django.forms.models import inlineformset_factory
    GAFormset = inlineformset_factory(Group, Group_Access, fields=['user', 'is_admin'])

    form = GAFormset(request.POST or None, instance=group)

    if form.is_valid():
        ga = form.save()
        #ga.save()
        messages.success(request, 'Usuário adicionado ao grupo com sucesso')

        return redirect('group_details', pk)

    return render(request, 'groups/group_add_member.html', {'form': form, 'pk': pk})


@login_required
def trip_list(request):
    grupos = Group_Access.objects.filter(user=request.user)
    from trip.models import Trip

    publicos = Trip.objects.filter(is_public=True)

    return render(request, 'groups/trip_list.html', { 'grupos': grupos, 'publicos': publicos  })
