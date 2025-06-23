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

def f404(request):
    return render(request, '404.html')

def instituion_facilities(request):
    return render(request, 'instituion_facilities.html')

def event_details(request):
    return render(request, 'event-details.html')

def news_details(request):
    return render(request, 'news-details.html')

def news(request):
    return render(request, 'news.html')

def privacy(request):
    return render(request, 'privacy.html')

def staff(request):
    return render(request, 'staff.html')

def stater_page(request):
    return render(request, 'stater-page.html')

def terms_of_service(request):
    return render(request, 'terms-of-service.html')

def student_life(request):
    return render(request, 'student-life.html')