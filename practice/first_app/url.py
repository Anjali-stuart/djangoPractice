from django.urls import path
from . import views

urlpatterns = [
               path('services', views.services, name = 'services'),
               path('', views.index, name = 'index'),
               path('base', views.home, name = 'home'),
               path('about', views.about, name = 'about'),
               path('contact', views.contact, name = 'contact'),
               ]

