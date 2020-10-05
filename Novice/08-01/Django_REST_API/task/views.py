from django.shortcuts import render
from rest_framework import viewsets
from .models import Pekerjaan
from .serializers import PekerjaanSerializer
# Create your views here.

class PekerjaanView(viewsets.ModelViewSet):
    serializer_class = PekerjaanSerializer
    queryset = Pekerjaan.objects.all()
#def index(request):
    #comments = [
        #{'nama' : 'Joko Kendil',
        #'motto' : 'Royco'},
        #{'nama' : 'Surya Piningit',
        #'motto' : 'Masako'}
    #]

    #return JsonResponse(comments, safe=False)