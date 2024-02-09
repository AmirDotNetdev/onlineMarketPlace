from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'contact'),
    path('contact/', views.contact, name = 'contact'),
]
