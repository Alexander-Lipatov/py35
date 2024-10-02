from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import City
# Create your views here.


def index(r):
    data = {
        'title':'Главная страница',
        'cities':City.objects.all().order_by('name')
    }
    return render(r, './main.html', data)


def news(r):
    
    
    try:
        city_id = r.COOKIES["city_id"]
        city = City.objects.get(id=city_id)
        data = {
            'title':'Новости',
            'city':city,
            'news':city.news.all()
        }
        if city_id:
            return render(r, './news.html', data)
    
    except Exception:
   
        return redirect(reverse('index'))
    


   


def managers(r):

    try:
        city_id = r.COOKIES["city_id"]
        data = {
            'title':'Управляющие',
            'city':City.objects.get(id=city_id)
        }
        if city_id:
            return render(r, './managers.html', data)
    
    except Exception:
   
        return redirect(reverse('index'))
    

    
    


def facts(r):

    try:
        city_id = r.COOKIES["city_id"]

        data = {
            'title':'Факты',
            'city':City.objects.get(id=city_id)
        }
        
        if city_id:
            return render(r, './facts.html', data)
    
    except Exception:
        return redirect(reverse('index'))
   


def contacts(r):

    try:
        city_id = r.COOKIES["city_id"]
        data = {
            'title':'Контакты',
            'city':City.objects.get(id=city_id)
        }
        
        if city_id:
            return render(r, './contacts.html', data)
    
    except Exception:
   
        return redirect(reverse('index'))
    
    


def city_detail(r, city_id):
   
    response = HttpResponseRedirect(reverse('news'))
    response.set_cookie('city_id', city_id, max_age=None)
    return response