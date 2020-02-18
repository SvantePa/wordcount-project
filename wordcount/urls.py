

from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name = 'homepage'),
    path('count/', views.count, name = 'countpage'),
    path('about/', views.about, name = 'aboutpage'),
]
