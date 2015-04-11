from uuid import uuid4
from django.db import models
from django.contrib.auth.models import User
from django.utils.functional import cached_property


class Group(models.Model):
    name = models.CharField(max_length=200, default='Desconhecido')
    is_public = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User)

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('group_details', args=[str(self.id)])

    def __unicode__(self):
        return self.name


class Group_Access(models.Model):
    group = models.ForeignKey(Group)
    user = models.ForeignKey(User)
    is_admin = models.BooleanField(default=False)
