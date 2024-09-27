from django.shortcuts import render

# Create your views here.


def index(r):
    data = {
        'title':'Главная страница'
    }
    return render(r, './main.html', data)


def news(r):
    data = {
        'title':'Новости'
    }
    return render(r, './news.html', data)


def managers(r):
    data = {
        'title':'Управляющие'
    }
    return render(r, './managers.html', data)


def facts(r):
    data = {
        'title':'Факты'
    }
    return render(r, './facts.html', data)


def contacts(r):
    data = {
        'title':'Контакты'
    }
    return render(r, './contacts.html', data)
