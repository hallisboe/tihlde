"""tihlde URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include


from landing.urls import landing_patterns
from events.urls import events_patterns
from news.urls import news_patterns

from ads.urls import ads_patterns

urlpatterns = [
	path('', include(landing_patterns)),
	path('arrangement/', include(events_patterns)),
	path('nyheter/', include(news_patterns)),
    path('karriere/', include(ads_patterns)),
	path('admin/', admin.site.urls),
]
