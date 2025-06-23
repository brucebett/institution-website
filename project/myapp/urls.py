from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('admision/', views.admision, name='admision'),
    path('academics/', views.academics, name='academics'),
    path('alumni/', views.alumni, name='alumni'),
    path('event/', views.event, name='event'),
]
