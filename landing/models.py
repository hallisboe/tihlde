from django.db import models

# Create your models here.


class Post(models.Model):
	published = models.DateTimeField(auto_now_add=True)
	edited = models.DateTimeField(auto_now=True)
