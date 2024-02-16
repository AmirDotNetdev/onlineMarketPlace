from django.urls import path
from .views import *

app_name = 'conversation'
urlpatterns = [
    path('new/<int:pk_item>/' , new_conversation, name='new'),
    path('detail/<int:pk>/' , detail, name='detail'),
    path('', inbox, name = 'inbox')
]
