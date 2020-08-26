from django.shortcuts import render, redirect



from . import models

def index(req):
    if req.POST:
        print(req.POST)
        models.Tugas.objects.create(Task=req.POST['name'])

    data = models.Tugas.objects.all()
    return render(req, 'list/index.html', {
        'data': data,
    })

def detail(req, id):
    data = models.Tugas.objects.filter(pk=id).first()
    return render(req, 'list/detail.html', {
        'data' : data,
    })

def delete(req, id):
    models.Tugas.objects.filter(pk=id).delete()
    return redirect('/')
