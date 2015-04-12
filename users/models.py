# encoding: iso-8859-1
from django.db import models
from django.contrib.auth.models import User


MOTO_CATEGORIES = list(sorted([
	('street', 'Street'),
	('naked', 'Naked'),
	('custom', 'Custom'),
	('crossover', 'Crossover'),
	('sport', 'Sport'),
	('touring', 'Touring'),
	('trail', 'Trail'),
	('scooter', 'Scooter'),
]))

UF_CHOICES = list(sorted([
    ('AC', 'Acre'), 
    ('AL', 'Alagoas'),
    ('AP', 'Amapá'),
    ('BA', 'Bahia'),
    ('CE', 'Ceará'),
    ('DF', 'Distrito Federal'),
    ('ES', 'Espírito Santo'),
    ('GO', 'Goiás'),
    ('MA', 'Maranão'),
    ('MG', 'Minas Gerais'),
    ('MS', 'Mato Grosso do Sul'),
    ('MT', 'Mato Grosso'),
    ('PA', 'Pará'),
    ('PB', 'Paraíba'),
    ('PE', 'Pernanbuco'),
    ('PI', 'Piauí'),
    ('PR', 'Paraná'),
    ('RJ', 'Rio de Janeiro'),
    ('RN', 'Rio Grande do Norte'),
    ('RO', 'Rondônia'),
    ('RR', 'Roraima'),
    ('RS', 'Rio Grande do Sul'),
    ('SC', 'Santa Catarina'),
    ('SE', 'Sergipe'),
    ('SP', 'São Paulo'),
    ('TO', 'Tocantins')
]))

SEX_CHOICES = (('M', 'Masculino'),
				('F', 'Feminino'),
				('O', 'Outro'))

class UserProfile(models.Model):
	 user = models.OneToOneField(User)

	 name = models.CharField("Nome", max_length=30)
	 sex = models.CharField("Sexo", max_length=10, blank=True, choices=SEX_CHOICES)

	 city = models.CharField("Cidade", max_length=100)
	 state = models.CharField("Estado", choices=UF_CHOICES, max_length=2)

	 motorcycle = models.CharField("Modelo", max_length=200, blank=True, null=True)
	 cc = models.PositiveIntegerField("Cilindrada", blank=True, null=True)
	 year = models.PositiveIntegerField("Ano", blank=True, null=True)

	 category = models.CharField("Categoria", choices=MOTO_CATEGORIES, null=True, max_length=200)
	 manufactured = models.CharField("Fabricante", blank=True, null=True, max_length=20)


	 def __unicode__(self):
	 	return "%s - %s (%s)" % (self.user, self.motorcycle, self.category)

from django.db.models.signals import post_save

def create_profile(sender, instance, created, raw, using, update_fields, *args, **kwargs):
	if created:
		new_profile = UserProfile(user=instance, name=instance.get_full_name())
		new_profile.save()

post_save.connect(create_profile, sender=User)