import datetime
from django.db import models
from django.utils import timezone
# Create your models here.

class Twit(models.Model):
	text = models.CharField(max_length=140)
	date = models.DateTimeField('date twitted')

	def __unicode__(self):
		return self.text

	def was_published_recently(self):
		return self.date >= timezone.now() - datetime.timedelta(days=1)
