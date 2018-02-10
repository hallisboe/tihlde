from django.db import models


from landing.models import Post
# Create your models here.


class Event(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()
	start = models.DateTimeField()
	end = models.DateTimeField()
	location = models.CharField(max_length=100)
	spots = models.IntegerField()
	opens = models.DateTimeField()

	slug = models.SlugField(max_length=100)

	def participants(self):
		return Participant.objects.filter(event=self).count()


	def is_full(self):
		return Participant.objects.filter(event=self).count() >= self.spots

	participants = property(participants)

	def __str__(self):
		return self.name


class Program(models.Model):
	identifier = models.CharField(max_length=100)

	def __str__(self):
		return self.identifier


class Grade(models.Model):
	identifier = models.CharField(max_length=100)

	def __str__(self):
		return self.identifier


class Participant(models.Model):
	event = models.ForeignKey(Event, on_delete='CASCADE')
	name = models.CharField(max_length=100)
	phone = models.CharField(max_length=20)
	email = models.CharField(max_length=100)
	allergies = models.CharField(max_length=100)
	program = models.ForeignKey(Program, on_delete='CASCADE')
	grade = models.ForeignKey(Grade, on_delete='CASCADE')

	def __str__(self):
		return self.name

