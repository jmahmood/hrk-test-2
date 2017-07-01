from django.shortcuts import render
from django.http import HttpResponse
import logging

from .models import Birthday

def index(request):
    return HttpResponse('Hello World')