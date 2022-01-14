from django.shortcuts import render
from django.views import generic
from .utilities import results

def cross(request):
    markets =  sorted([(v, k) for k, v in results.items()], reverse=True)
    return render(request, 'index.html', {'markets':markets})
