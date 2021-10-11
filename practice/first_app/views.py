from django.shortcuts import render
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
    return render(request, 'contact.html')
    # retur.'/'.'jn HttpResponse("this is contact us page.")
def services(request):
    return render(request, 'contact.html')
# Create your views here.
# def add_show(request):
#     return render(request, 'first_app/addandShow.html'),