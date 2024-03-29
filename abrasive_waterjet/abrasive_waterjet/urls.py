"""abrasive_waterjet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from .views import MainPage, Dashboard
from django.views.generic import TemplateView


urlpatterns = [
    path("", MainPage.as_view(), name="main-page"),
    path("aboutme/", TemplateView.as_view(template_name="home/aboutme.html"), name="aboutme"),
    path("dashboard/", Dashboard.as_view(), name="dashboard"),
    path("admin/", admin.site.urls),
    path("cut/", include("cutting_performance.urls")),
    path("plot/", include("cutting_plots.urls")),
    path("users/", include('users.urls')),

    
    
]
