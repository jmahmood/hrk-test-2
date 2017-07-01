from django.shortcuts import render
from django.http import HttpResponse
import logging
import requests

def index(request):
    logging.warning('Hello World executed on warm-forest-44218')
    requests.post("https://still-basin-26156.herokuapp.com/logs", "Hello World executed on warm-forest-44218")
    return HttpResponse('Hello World')