from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('safe/', views.safe, name='safe'),
]