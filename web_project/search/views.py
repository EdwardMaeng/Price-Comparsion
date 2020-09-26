from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
import re
import urllib

# Create your views here.
def home(request):
    return HttpResponse("Hello, Django!")

def search(request):
    return render(
        request,
        'search/search.html', {}
    )

def result(request, product):
    # Run ALL Scraping in here
    lists = ["HELLO", "My", "Name", "is", "Yohan", "Kim"]
    return render(
        request,
        'search/result.html', 
        {
            'product': product,
            'lists': lists,
        }
    )