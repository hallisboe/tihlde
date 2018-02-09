from django.shortcuts import render

# Create your views here.

from news.models import Article
from events.models import Event


def index(request):
	return render(request, 'landing/index.html', {'articles': Article.objects.all(), 'events': Event.objects.all()})