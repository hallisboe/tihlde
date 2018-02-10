from django.db import models
from django.utils.safestring import mark_safe
# Create your models here.

from landing.models import Post


class Article(Post):
	title = models.CharField(max_length=100)
	ingress = models.CharField(max_length=200)
	body = models.TextField()

	slug = models.SlugField(max_length=100)

	image_url = models.URLField(blank=True, max_length=1000)

	def __str__(self):
		return self.title 