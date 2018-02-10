from django.shortcuts import render

from django.urls import reverse
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormMixin

from .forms import ParticipantForm
from .models import Event

# Create your views here.


def index(request):
	return render(request, 'events/index.html', {})

class EventDetailView(FormMixin, DetailView):
    model = Event
    form_class = ParticipantForm

    def get_success_url(self):
        return reverse('landing:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        if not self.object.is_full():
            participant = form.save(commit=False)
            participant.event = self.object
            participant.save()
            ## Send email
        return super().form_valid(form)


class EventListView(ListView):
    model = Event
