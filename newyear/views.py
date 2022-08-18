from django.shortcuts import render

import datetime

def index(request):
    now = datetime.datetime.now()
    return render(request, "newyear/index.html", {
        'newyear': now.day == 18 and now.month == 8 
    })