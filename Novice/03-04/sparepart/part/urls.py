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
    path('show2', views.show2),
    path('edit2/<int:id>', views.edit2),  
    path('update2/<int:id>', views.update2),  
    path('delete2/<int:id>', views.destroy2),  
]
