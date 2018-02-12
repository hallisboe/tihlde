from django.shortcuts import render

# Create your views here.

from news.models import Article
from events.models import Event
from .models import Post

def index(request):
	return render(request, 'landing/index.html', {'posts': Post.objects.all().order_by('-published'), 'events': Event.objects.all().order_by('start')[:6]})

def about(request):
	return render(request, 'landing/about.html', {})

def intro(request):
	return render(request, 'landing/intro.html', {})

def promo(request):
	return render(request, 'landing/promo.html', {})

def services(request):
	return render(request, 'landing/services.html', {})

def volenteers(request):
	return render(request, 'landing/volenteers.html', {})