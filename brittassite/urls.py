"""brittassite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from brittas_blog.views import home
from brittas_blog.views import jewelry
from brittas_blog.views import art
from brittas_blog.views import about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('jewelry/', jewelry, name='jewelry'),
    path('art/', art, name='art'),
    path('about/', art, name='about'),
]