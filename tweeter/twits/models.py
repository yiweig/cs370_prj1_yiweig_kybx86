import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Twit(models.Model):
	text = models.CharField(max_length=140)
	user = models.ForeignKey(User)
	created_date = models.DateTimeField(auto_now=True, blank=False)

	def __unicode__(self):
		return self.text

	def was_published_recently(self):
		return self.created_date >= timezone.now() - datetime.timedelta(days=1)

class Twitter(models.Model):
	name = models.OneToOneField(User)
	following = models.ManyToManyField('self', related_name='followers', symmetrical=False)
