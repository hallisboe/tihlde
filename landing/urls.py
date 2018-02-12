from django.urls import path


from . import views

landing_patterns = ([
    path('', views.index, name='list'),
    path('om-oss/', views.about, name='about'),
    path('ny-student/', views.intro, name='intro'),
    path('for-bedrifter/', views.promo, name='promo'),
    path('tjenester/', views.services, name='services'),
    path('frivillige/', views.volenteers, name='volenteers'),
], 'landing')
