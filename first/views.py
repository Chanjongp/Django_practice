from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from django.template import loader
from datetime import datetime
import random


def index(request):
    now = datetime.now()
    context = {
        'current_date' : now
    }
    return render(request, 'first/index.html', context)


def select(request):
    context = {}
    return render(request, 'first/select.html', context)

def result(request):
    chosen = int(request.GET['number'])
    results = []
    if chosen >= 1 and chosen <=  45:
        results.append(chosen)
    
    box = []
    for i in range(0, 45):
        if chosen != i+1: # range는 0부터 44이기 때문에 i+1을 하면 로또번호가 됌
                box.append(i+1)
    
    random.shuffle(box)

    while len(results) < 6:
        results.append(box.pop())

    context = {
        'numbers' : results
    }
    return render(request, 'first/result.html', context)