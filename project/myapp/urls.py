from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('admision/', views.admision, name='admision'),
    path('academics/', views.academics, name='academics'),
    path('alumni/', views.alumni, name='alumni'),
    path('about/', views.about, name='about'),
    path('event/', views.event, name='event'),
    path('f404/', views.f404, name='f404'),
    path('event_details/', views.event_details, name='event_details'),
    path('news_details/', views.news_details, name='news_details'),
    path('news/', views.news, name='news'),
    path('privacy/', views.privacy, name='privacy'),
    path('staff/', views.staff, name='staff'),
    path('stater_page/', views.stater_page, name='stater_page'),
    path('student_life/', views.student_life, name='student_life'),
    path('terms_of_service/', views.terms_of_service, name='terms_of_service'),
    path('institution_facilities/', views.institution_facilities, name='institution_facilities'),
]
