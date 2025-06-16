from django.urls import path
from myapp import views

urlpatterns = [
    path('contact/', views.contact, name='contact')
]
