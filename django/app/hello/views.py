from django.shortcuts import render
from datetime import datetime, date, timedelta
from typing import List,Dict
# Create your views here.
from django.http import response

def multiplication_table_dict():
    data:List[Dict] = []

    for i in range(10):
        row = {i+1: {j+1: (i+1)*(j+1) for j in range(10)}}
        data.append(row)
    return data

data = {
        'hello': 'Hello, Django!',
        'date':datetime.now(),
        'table': multiplication_table_dict(),
         
    }


def index(r):
    return render(r, './date_now.html', data)


def table_mult(r):
    return render(r, './table_mult.html', data)



def dev_day(r):
    data_now = date(datetime.now().year, 1, 1) + timedelta(days=256)
    
    return render(r, './dev_day.html', {'dev_day': data_now})