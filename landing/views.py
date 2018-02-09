from django.shortcuts import render

# Create your views here.

from news.models import Article


def index(request):
	return render(request, 'landing/index.html', {'articles': Article.objects.all()})