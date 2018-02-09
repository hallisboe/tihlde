from django.urls import path


from . import views

landing_patterns = ([
    path('', views.index, name='list'),
], 'landing')
