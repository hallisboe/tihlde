from django.shortcuts import render

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Ad
# Create your views here.

class AdDetailView(DetailView):
    model = Ad


class AdListView(ListView):
    model = Ad