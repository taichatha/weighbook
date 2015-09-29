from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Log(models.Model):
	user = models.ForeignKey(User)
	date = models.DateTimeField('Date Published')

	def __unicode__(self):
		return self.date

class Lift(models.Model):
	lift_name = models.CharField(max_length=200)

	def __unicode__(self):
		return self.lift_name

class Set(models.Model):
	log = models.ForeignKey(Log)
	lift = models.ForeignKey(Lift, default = None )
	reps = models.IntegerField(blank = True)

	