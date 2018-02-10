from django.db import models

# Create your models here.

from landing.models import Post


class Article(Post):
	title = models.CharField(max_length=100)
	ingress = models.CharField(max_length=200)
	body = models.TextField()

	slug = models.SlugField(max_length=100)

	def __str__(self):
		return self.title 