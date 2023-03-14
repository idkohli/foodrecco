from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('recco', views.recco, name='recco'),
    path('add', views.add, name='add')
]