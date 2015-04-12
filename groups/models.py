# encoding: iso-8859-1

from uuid import uuid4
from django.db import models
from django.contrib.auth.models import User
from django.utils.functional import cached_property


class Group(models.Model):
    name = models.CharField("Nome", max_length=200)
    is_public = models.BooleanField("Grupo Público?", default=False)
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

    class Meta:
    	unique_together = ['group', 'user']


from django.db.models.signals import post_save

def create_access(sender, instance, created, raw, using, update_fields, *args, **kwargs):
	if created:
		new_access = Group_Access(group=instance, user=instance.owner, is_admin=True)
		new_access.save()

post_save.connect(create_access, sender=Group)