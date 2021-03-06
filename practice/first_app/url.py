from django.urls import path
from . import views

urlpatterns = [
               path('services', views.services, name = 'services'),
               path('', views.index, name = 'home'),
               path('base', views.home, name = 'base'),
               path('about', views.about, name = 'about'),
               path('contact', views.contact, name = 'contact'),
               path('submit', views.submit, name = 'submit')
               ]

