from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
import re

# Create your views here.
def home(request):
    return HttpResponse("Hello, Django!")

def hello_there(request):
    return render(
        request,
        'search/hello_there.html',{}
    )