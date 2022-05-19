
from django.shortcuts import render
from django.views import generic
from .models import *
# Create your views here.

class CarView(generic.ListView):
    model = Samochod

    def get_queryset(self):
        return Samochod.objects.all()


class KierowcaView(generic.ListView):
    model = Kierowca

    def get_queryset(self):
        return Kierowca.objects.all()

