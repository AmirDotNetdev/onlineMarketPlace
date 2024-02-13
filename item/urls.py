from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.detail, name= 'detail'),
    path('<int:pk>/delete/', views.delete, name= 'delete'),
    path('<int:pk>/edit/', views.edit, name= 'edit'),
    path('new/', views.new, name= 'new'),
    path('browser/', views.items, name= 'browser'),
]
