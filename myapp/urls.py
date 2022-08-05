from django.contrib import admin
from django.urls import path
from myapp import views
from .views import employeesList

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('service', views.service, name='service'),
    path('employees/',employeesList.as_view()),
    path('employees/<int:id>/', employeesList.as_view()),

]