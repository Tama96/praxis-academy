from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Pekerjaan

def index(req):
    data = Pekerjaan.objects.all()
    simpan = []
    for d in data:
        simpan.append({
            'nama':d.nama,
            'motto':d.motto
        })
    return JsonResponse({
        'data':simpan
    })

def create(req):
    

# class PekerjaanView(viewsets.ModelViewSet):
#     serializer_class = PekerjaanSerializer
#     queryset = Pekerjaan.objects.all()

# def index(request):
#     comments = [
#         {'nama' : 'Joko Kendil',
#         'motto' : 'Royco'},
#         {'nama' : 'Surya Piningit',
#         'motto' : 'Masako'}
#     ]

#     return JsonResponse(comments, safe=False)

# def show(request):
#     datas = 
