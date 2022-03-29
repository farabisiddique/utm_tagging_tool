"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from mysite.views import home_view
from mysite.views import show_utm
from mysite.views import scrape_linkedin
from mysite.views import scrape_google


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view ),
    path('showutm/', show_utm ),
    path('scrape/', scrape_linkedin ),
    path('scrapeg/', scrape_google ),

]
