from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


# Create your views here.

def base(response):
    return render(response, 'locky/base.html')


def home(response):
    return render(response, 'locky/home.html')