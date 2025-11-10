from django.shortcuts import render
from .models import productinfo, offerinfo

# Create your views here.
def index(request):
    offerproducts = offerinfo.objects.all()
    context = {
        'offerproducts': offerproducts,
    }
    return render(request, 'index.html', context)

def Store(request):
    products = productinfo.objects.all()
    context = {
        'products': products,
    }
    
    return render(request, 'store.html', context)

def contact(request):
    return render(request, 'contact.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')