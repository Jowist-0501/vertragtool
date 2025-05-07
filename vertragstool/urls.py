"""
URL configuration for vertragstool project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from vertrag import views

urlpatterns = [
    path("admin/", admin.site.urls),
    # Tätigkeiten
    path('taetigkeiten/', views.taetigkeiten_liste, name='taetigkeiten_liste'),
    path('taetigkeiten/neu/', views.taetigkeiten_erstellen, name='taetigkeiten_erstellen'),
    path('taetigkeiten/<int:pk>/bearbeiten/', views.taetigkeiten_bearbeiten, name='taetigkeiten_bearbeiten'),
    path('taetigkeiten/<int:pk>/loeschen/', views.taetigkeiten_loeschen, name='taetigkeiten_loeschen'),
    #Firmen
    path('firmen/', views.firmen_liste, name='firmen_liste'),
    path('firmen/neu/', views.firmen_erstellen, name='firmen_erstellen'),
    path('firmen/<int:pk>/bearbeiten/', views.firmen_bearbeiten, name='firmen_bearbeiten'),
    path('firmen/<int:pk>/loeschen/', views.firmen_loeschen, name='firmen_loeschen'),
]
