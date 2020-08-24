from django.shortcuts import render



from . import models

def index(req):
    if req.POST:
        print(req.POST)
        models.Tugas.objects.create(Task=req.POST['name_field'])

    data = models.Tugas.objects.all()
    return render(req, 'list/index.html', {
        'data': data,
    })