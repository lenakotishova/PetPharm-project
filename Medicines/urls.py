from django.urls import path
import Medicines.views

urlpatterns = [
    path('test/', Medicines.views.index1),
    path('', Medicines.views.index),
]