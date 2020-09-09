from django.contrib import admin
from django.urls import path
from pekerja import views

urlpatterns = [
    # from Pekerja
    path('home', views.home),
    path('show_pegawai', views.show_pegawai),
    path('edit_pegawai/<int:id>', views.edit_pegawai),  
    path('update_pegawai/<int:id>', views.update_pegawai),  
    path('delete_pegawai/<int:id>', views.destroy_pegawai),
]