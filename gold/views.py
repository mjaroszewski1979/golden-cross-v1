from django.shortcuts import render
from .utilities import indis

def cross(request):
    zipped_list = zip(indis.values, indis.results, indis.names)
    return render(request, 'index.html', {"context":zipped_list})
