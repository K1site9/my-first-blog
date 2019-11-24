from django.shortcuts import render
from django.http.response import HttpResponse
from datetime import datetime

# Create your views here.

def test(request):
    return render(request, 'test.html')