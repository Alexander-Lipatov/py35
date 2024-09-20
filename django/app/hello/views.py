from django.shortcuts import render

# Create your views here.
from django.http import response

def index(r, slug):

    print(slug)
    return render(r, 'hello/index.html', {'message': 'Hello, Django!'})