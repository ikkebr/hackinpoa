# encoding: iso-8859-1
from django.db import models
from django.contrib.auth.models import User


MOTO_CATEGORIES = (
	('Street', 'street'),
	('Naked', 'naked'),
	('Custom', 'custom'),
	('Crossover', 'crossover'),
	('Sport', 'sport'),
	('Touring', 'touring'),
	('Trail', 'trail'),
	('Scooter', 'scooter'),
)

UF_CHOICES = (
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
)

SEX_CHOICES = (('Male', 'M'),
				('Female', 'F'),
				('Other', 'O'))

class UserProfile(models.Model):
	 user = models.OneToOneField(User)

	 name = models.CharField(max_length=30)
	 sex = models.CharField(max_length=10, blank=True, choices=SEX_CHOICES)

	 city = models.CharField(max_length=100)
	 state = models.CharField(choices=UF_CHOICES, max_length=2)

	 motorcycle = models.CharField(max_length=200, blank=True, null=True)
	 cc = models.PositiveIntegerField(blank=True, null=True)
	 year = models.PositiveIntegerField(blank=True, null=True)

	 category = models.CharField(choices=MOTO_CATEGORIES, null=True, max_length=200)
	 manufactured = models.CharField(blank=True, null=True)


	 def __unicode__(self):
	 	return "%s - %s (%s)" % (self.user, self.motorcycle, self.category)

from django.db.models.signals import post_save

def create_profile(sender, instance, created, raw, using, update_fields):
	if created:
		new_profile = UserProfile(user=sender, nome=sender.first_name+" "+sender.last_name)
		new_profile.save()
