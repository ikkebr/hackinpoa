from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse
from .models import *
from django.contrib.auth.models import User

class GroupDetailTests(TestCase):
    def setUp(self):
        self.c = Client(enforce_csrf_checks=False)
        self.user = User.objects.create_user('dummy', 'dummy@henrique.email', 'dummy')
        self.user.is_superuser = True
        self.user.save()

        self.ouser = User.objects.create_user('dummy2', 'dummy2@henrique.email', 'dummy2')
        self.ouser.is_superuser = False
        self.ouser.save()

        self.grupo_a = Group.objects.create(id=1, is_public=0, name='foo', owner=self.user)
        self.grupo_a.save()

        self.grupo_b = Group.objects.create(id=2, is_public=0, name='baz', owner=self.user)
        self.grupo_b.save()

        Group_Access.objects.all().delete()

        self.acesso_a = Group_Access.objects.create(group=self.grupo_a, user=self.user)
        self.acesso_a.save()


    def teste_usuario_anonimo_retorna_302(self):
        response = self.c.get(reverse("group_details", args=[1,]))
        self.assertEqual(response.status_code, 302)

    def teste_usuario_logado_com_acesso_retorna_200(self):
        self.c.login(username='dummy', password='dummy')
        response = self.c.get(reverse("group_details", args=[self.acesso_a.group.id]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['currpage'], 'isall')
        
    def teste_usuario_logado_today_com_query(self):
        self.c.login(username='dummy', password='dummy')
        response = self.c.get(reverse("group_details", args=[self.acesso_a.group.id]), {'q': 'BAR'})
        self.assertEqual(response.status_code, 200)
        
    def teste_usuario_nao_logado_today_com_query(self):
        response = self.c.get(reverse("group_details", args=[self.acesso_a.group.id]), {'q': 'BAR'})
        self.assertEqual(response.status_code, 302) #login


    def teste_admin_logado_sem_acesso_retorna_200(self):
        self.c.login(username='dummy', password='dummy')
        self.user.is_superuser = True
        response = self.c.get(reverse("group_details", args=[2,]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['currpage'], 'isall')

    def teste_usuario_logado_sem_acesso_retorna_404(self):
        self.c.login(username='dummy2', password='dummy2')
        self.user.is_superuser = False
        self.user.save()
        response = self.c.get(reverse("group_details", args=[2,]))
        self.assertEqual(response.status_code, 404)

    def teste_usuario_logado_today_sem_acesso_retorna_404(self):
        self.c.login(username='dummy2', password='dummy2')
        self.user.is_superuser = False
        self.user.save()
        response = self.c.get(reverse("group_details", args=[2,]))
        self.assertEqual(response.status_code, 404)



class GroupListTests(TestCase):
    def setUp(self):
        self.c = Client()
        self.user = User.objects.create_user('dummy', 'dummy@henrique.email', 'dummy')
        self.user.is_superuser = True
        self.user.save()

        grupo_a = Group.objects.create(is_public=0, name='baz', owner=self.user)
        grupo_a.save()

        grupo_b = Group.objects.create(is_public=0, name='foo', owner=self.user)
        grupo_b.save()

        Group_Access.objects.all().delete()

        acesso_a = Group_Access.objects.create(group=grupo_a, user=self.user)
        acesso_a.save()


    def teste_usuario_anonimo_retorna_302(self):
        response = self.c.get(reverse("groups"))
        self.assertEqual(response.status_code, 302)

    def teste_usuario_logado_retorna_200(self):
        self.c.login(username='dummy', password='dummy')
        response = self.c.get(reverse("groups"))
        self.assertEqual(response.status_code, 200)


    def teste_usuario_admin_ve_todos_os_grupos(self):
        self.c.login(username='dummy', password='dummy')

        response = self.c.get(reverse("groups"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual( len(response.context["object_list"]), 2)

    def teste_usuario_normal_ve_seus_grupos(self):
        self.user.is_superuser = False
        self.user.save()
        self.c.login(username='dummy', password='dummy')

        response = self.c.get(reverse("groups"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual( len(response.context["object_list"]), 1)


class GroupCreateTests(TestCase):
    def setUp(self):
        self.c = Client()
        self.user = User.objects.create_user('dummy', 'dummy@henrique.email', 'dummy')
        self.user.save()

        self.user2 = User.objects.create_user('adummy', 'adummy@henrique.email', 'adummy')
        self.user2.save()

        self.user3 = User.objects.create_user('fdummy', 'fdummy@henrique.email', 'fdummy')
        self.user3.save()

        self.grupo_a = Group.objects.create(id=1, name="abcd", is_public=0, owner=self.user)
        self.grupo_a.save()

        acesso_a = Group_Access.objects.create(group=self.grupo_a, user=self.user3)
        acesso_a.save()


    def teste_usuario_anonimo_retorna_302(self):
        response = self.c.get(reverse("group_create"))
        self.assertEqual(response.status_code, 302)

    def teste_usuario_logado_retorna_200(self):
        self.c.login(username='dummy', password='dummy')
        response = self.c.get(reverse("group_create"))
        self.assertEqual(response.status_code, 200)

