from django.shortcuts import render,redirect
from . import models, forms

def input(req):
    form_input = forms.penggunaForm()
    if req.POST:
        form_input = forms.penggunaForm(req.POST)
        if form_input.is_valid():
            form_input.save()
        return redirect('/')
    pengguna = models.Pengguna.objects.all()
    return render(req,'input.html',{
        'form':form_input,
        'data':pengguna,
    })
def detail(req, id):
    pengguna = models.Pengguna.objects.filter(pk=id).first()    
    return render(req, 'detail.html', {
        'data': pengguna,
    })
def index(req):
    pengguna = models.Pengguna.objects.all()
    return render(req, "index.html", {
        'data': pengguna
    })
def update(req, id):
    if req.POST:
        pengguna = models.Pengguna.objects.filter(pk=id).update(nama=req.POST['nama'], username=req.POST['username'], password=req.POST['password'])
        return redirect('/')

    pengguna = models.Pengguna.objects.filter(pk=id).first()    
    return render(req, 'update.html', {
        'data': pengguna,
    })
def delete(req, id):
    models.Pengguna.objects.filter(pk=id).delete()
    return redirect('/')