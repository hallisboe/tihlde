from django.urls import path


from . import views

news_patterns = ([
    path('', views.ArticleListView.as_view(), name='list'),
    path('<slug:slug>/', views.ArticleDetailView.as_view(), name='detail'),
], 'article')
