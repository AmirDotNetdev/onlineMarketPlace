from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm
urlpatterns = [
    path('', views.index,),
    path('contact/', views.contact, name = 'contact'),
    path('signup/', views.signUp, name = 'signup'),
    path('logout/', views.logout, name = 'logout'),
    path('login/', auth_views.LoginView.as_view(template_name = 'core/login.html', authentication_form = LoginForm), name = 'login'),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
