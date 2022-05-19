from django.urls import path
from .views import *


app_name='cars'

urlpatterns=[
    path('brand', CarView.as_view(), name='type-list'),
    path('driver', KierowcaView.as_view(), name='type-list'),
    path('insurance', UbezpieczenieView.as_view(), name='type-list'),
]