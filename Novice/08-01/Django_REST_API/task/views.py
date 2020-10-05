from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

def index(request):
    comments = [
        {'nama' : 'Joko Kendil',
        'motto' : 'Royco'},
        {'nama' : 'Surya Piningit',
        'motto' : 'Masako'}
    ]

    return JsonResponse(comments, safe=False)