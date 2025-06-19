from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def contact(request):
    return render(request, 'contact.html')

def academics(request):
    return render(request, 'academics.html')

def alumni(request):
    return render(request, 'alumni.html')

def admision(request):
    return render(request, 'admision.html')

def event(request):
    return render(request, 'event.html')