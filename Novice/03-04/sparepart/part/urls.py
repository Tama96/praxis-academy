from django.contrib import admin
from django.urls import path
from part import views

urlpatterns = [
    # from Sparepart
    path('admin/', admin.site.urls),
    path('emp', views.emp),
    path('show', views.show),
    path('edit/<int:id>', views.edit),  
    path('update/<int:id>', views.update),  
    path('delete/<int:id>', views.destroy),
    # from Pekerja
    path('home', views.home),
    path('show_pegawai', views.show_pegawai),
    path('edit_pegawai/<int:id>', views.edit_pegawai),  
    path('update_pegawai/<int:id>', views.update_pegawai),  
    path('delete_pegawai/<int:id>', views.destroy_pegawai),
    # front page
    path('', views.menu),  
]
