from django.shortcuts import render, redirect
from datetime import datetime
from .models import Contact, Submit
from django.contrib import messages
from django.http import HttpResponse


def index(request):
    # messages.success(request," this is a test message.")
    return render(request, 'index.html')

    # return HttpResponse("Welcome to djang!,")


def home(request):
    context = {
        "varialbe": "this is sent."
    }
    return render(request, 'base.html', context)


def submit(request):
    if request.method == "post":
        name = request.post.get('name')
        print("name = ", name)
        phone = request.post.get('phone')
        print("phone = ", phone)
        submit = Submit(name=name, phone=phone, date = datetime.today())
        submit.save()
        messages.success(request, 'Message sent successfully.')

    return render(request, 'Myform.html')

def about(request):
    return render(request, 'about.html')
    # return HttpResponse("This is about us page.")


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        print("name  = ", name)
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        return redirect('/')

    all_contact = Contact.objects.all()
    # print("all contatc", all_contact)   # not showing any result in terminal
    context = {'all_contact': all_contact}
    return render(request, 'contact.html')


def services (request):
    return render(request, 'services.html')


