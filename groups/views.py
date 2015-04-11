import datetime

from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, DetailView, TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import Http404, HttpResponse
from django.contrib.auth import logout
from django import forms

from .models import Group, Group_Access

def logout_view(request):
    logout(request)
    return redirect('django.contrib.auth.views.login')


class LoginRequiredMixin(object):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)


class GroupCreate(LoginRequiredMixin, TemplateView):
    def get(self, request):
        return HttpResponse('Not implemented')

    def post(self, request):
        return HttpResponse('Not implemented')


class GroupList(LoginRequiredMixin, ListView):
    model = Group

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Group.objects.all()

        return Group.objects.filter(id__in=[each.group.id for each in Group_Access.objects.filter(user=self.request.user)])


class GroupDetail(LoginRequiredMixin, ListView):
    model = Group
    allow_empty = True
    paginate_by = 150

    def get_queryset(self):
        self.group = get_object_or_404(Group, id=self.kwargs['pk'])

        if not self.request.user.is_superuser:
            self.access = get_object_or_404(Group_Access, group=self.group, user=self.request.user)

        if self.request.user.is_superuser or self.access:

            return Group.objects.filter(id=self.group.id)

        raise Http404(u"Acesso negado a esse grupo.")

    def get_context_data(self, **kwargs):
        context = super(GroupDetail, self).get_context_data(**kwargs)
        context['grupo'] = self.group
        context['query'] = self.request.GET.get('q', '')
        context['currpage'] = 'isall'
        return context
