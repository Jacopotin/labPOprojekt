from .forms import app_Form
from django.shortcuts import render
from django.views import generic
from .models import *
# Create your views here.

class CarView(generic.ListView):
    model = Samochod
    template_name = "car_list.html"
    def get_queryset(self):
        return Samochod.objects.all()


class KierowcaView(generic.ListView):
    model = Kierowca
    template_name = "driver_list.html"
    def get_queryset(self):
        return Kierowca.objects.all()


class UbezpieczenieView(generic.ListView):
    model = Ubezpieczenie
    template_name = "insurance_list.html"
    def get_queryset(self):
        return Ubezpieczenie.objects.all()


def app_form(request):
    form=app_Form(request.POST or None)
    if form.is_valid():
        form.save()
    context={
    'form':form
    }
    return render(request,'app_forms.html',context)