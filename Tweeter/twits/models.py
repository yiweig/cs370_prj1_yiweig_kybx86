from django.db import models

# Create your models here.
class Twit(models.Model):
	twit_text = models.CharField(max_length=140)
	twit_date = models.DateTimeField('date twitted')
