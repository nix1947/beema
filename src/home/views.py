from django.shortcuts import render
from django.shortcuts import HttpResponse

def index(request):
    """Function to serve homepage"""
    return render(request, 'home_page.html', {})



def contact(request):
    return render(request, 'contact.html', {

    })
