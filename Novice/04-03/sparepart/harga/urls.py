from django.contrib import admin
from django.urls import path
from harga import views

urlpatterns = [
    # from Harga
    path('home_harga', views.home_harga),
    path('show_harga', views.show_harga),
    path('edit_harga/<int:id>', views.edit_harga),  
    path('update_harga/<int:id>', views.update_harga),  
    path('delete_harga/<int:id>', views.destroy_harga),  
]