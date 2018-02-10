from django.urls import path


from . import views



ads_patterns = ([
    path('<slug:slug>/', views.AdDetailView.as_view(), name='detail'),
    path('', views.AdListView.as_view(), name='list'),
], 'ad')
