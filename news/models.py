from django.db import models

# Create your models here.


class Article(models.Model):
	title = models.CharField(max_length=100)
	ingress = models.CharField(max_length=200)
	body = models.TextField()
	published = models.DateTimeField(auto_now_add=True)
	edited = models.DateTimeField(auto_now=True)

	slug = models.SlugField(max_length=100)

	def __str__(self):
		return self.title 