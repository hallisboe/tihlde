from django.db import models


from landing.models import Post
# Create your models here.


class Sponsor(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name

class Type(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name

class Ad(Post):
	sponsor = models.ForeignKey(Sponsor, on_delete='CASCADE')
	title = models.CharField(max_length=200)
	description = models.CharField(max_length=200)
	job = models.CharField(max_length=200)
	job_type = models.ForeignKey(Type, on_delete='CASCADE')
	deadline = models.DateTimeField()
	location = models.CharField(max_length=200)

	slug = models.SlugField(max_length=100)

	def __str__(self):
		return self.title


