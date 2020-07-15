from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('About-me/',  views.about, name='about'),
    path('Contact/', views.contact, name='contact'),
    path('Pricing/', views.pricing, name='pricing'),
    path('Daily-Quotes/', views.dailyquotes, name='dailyquotes'),
    path('News/', views.news, name='news'),
    path('Religion/', views.religion, name='religion'),
    path('Food/', views.food, name='food'),
    path('Sports/', views.sports, name='sports'),
    path('Fashion/', views.fashion, name='fashion'),
]
