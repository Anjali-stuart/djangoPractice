from django.shortcuts import render
from datetime import datetime
from .models import Contact
from django.http import HttpResponse


def index(request):
    return  render(request, 'index.html')
    # return HttpResponse("Welcome to djang!,")


def home(request):
    context = {
        "varialbe": "this is sent."
    }
    return render(request, 'base.html', context)


def about(request):
    return render(request, 'about.html')
    # return HttpResponse("This is about us page.")


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
    return render(request, 'contact.html')



def services(request):
    return render(request, 'contact.html')

