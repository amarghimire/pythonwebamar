from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(data ):
    return HttpResponse ('hello data newsapi')