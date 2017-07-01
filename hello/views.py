from django.shortcuts import render
from django.http import HttpResponse
import logging

def index(request):
    logging.warning('Hello World executed on warm-forest-44218')
    return HttpResponse('Hello World')