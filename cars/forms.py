from django import forms
from .models import *

class app_Form(forms.ModelForm):
    class Meta:
        model=Samochod
        fields=['rocznik','marka','model','kolor','generacja']
