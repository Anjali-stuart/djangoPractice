from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello,world. You're at the first_app interface")


def home(request):
    return render(request, template_name='base.html')
# Create your views here.
