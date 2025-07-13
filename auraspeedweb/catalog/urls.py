from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('catalogo/', views.catalog, name='catalog'),
    path('catalogo/', views.contact, name='contact'),
]