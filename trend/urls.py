from django.urls import path
from django.views.generic import TemplateView
from .views import cross

urlpatterns = [
    path('', cross, name='cross'),
]