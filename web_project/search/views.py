from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
import re
import urllib
import sys
sys.path.append("..")
import scraping

# Create your views here.
def search(request):
    return render(
        request,
        'search/search.html', {}
    )

def result(request, product):
    scraping_object = scraping.scraping(product)
    items = scraping_object.get_item_list
    return render(
        request,
        'search/result.html', 
        {
            'item': items,
        }
    )