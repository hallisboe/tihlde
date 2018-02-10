from django.urls import path


from . import views

events_patterns = ([
    path('<slug:slug>/', views.EventDetailView.as_view(), name='detail'),
    path('', views.EventListView.as_view(), name='list'),
], 'event')
