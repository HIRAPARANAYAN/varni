"""
URL configuration for varni project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include
from . import views

urlpatterns = [
    path('loginform/',include('authentication.urls'),name='loginform'),
    path('Dashboard/',include('adminDashboard.urls'),name='AdminDashboard'),
    path('CustmorDashboard/',include('Customer.urls'),name='CustomerDashboard'),
    path('admin/', admin.site.urls),
    path('',views.index, name='index'),
    path('company/',views.company, name='company'),
    path('contactus/',views.contactus, name='contactus'),
    path('marvel/',views.marvel, name='marvel'),
    path('universal/',views.universal, name='universal'),
    path('digitalloan/', views.digitalloan, name='digitalloan'),
    path('termsconditions/', views.termscond, name='termscond'),
    path('privacypolicy/', views.privacy, name='privacy'),
    path('membershipcardterms/', views.cardtc, name='cardtc'),



]