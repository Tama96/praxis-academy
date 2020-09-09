from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('', include("part.urls",)),
    path('', include("harga.urls",)),
    path('', include("pekerja.urls",)),
]
