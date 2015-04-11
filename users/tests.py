from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import resolve
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

class EditProfileTests(TestCase):

    def setUp(self):
        self.c = Client(enforce_csrf_checks=False)

    def teste_cadastro_anonimo_retorna_302(self):
        response = self.c.get(reverse("edit_profile"))
        self.assertEqual(response.status_code, 302)

    def teste_cadastro_usuario_autenticado_redireciona(self):
        user = User.objects.create_user(
            'dummy', 'dummy@henrique.email', 'dummy')
        self.c.login(username='dummy', password='dummy')
        response = self.c.get(reverse("edit_profile"))
        self.assertEqual(response.status_code, 200)