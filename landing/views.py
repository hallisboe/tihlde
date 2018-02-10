from django.shortcuts import render

# Create your views here.

from news.models import Article
from events.models import Event
from .models import Post

def index(request):
	return render(request, 'landing/index.html', {'posts': Post.objects.all().order_by('-published'), 'events': Event.objects.all()})