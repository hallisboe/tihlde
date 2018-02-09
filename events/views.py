from django.shortcuts import render


from django.views.generic.detail import DetailView
from django.views.generic.list import ListView


from .models import Event

# Create your views here.


def index(request):
	return render(request, 'events/index.html', {})

class EventDetailView(DetailView):
	model = Event


class EventListView(ListView):
	model = Event
