from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from . import models, forms
from django.contrib.auth.decorators import login_required

# Login & Signup
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def logout(request):
	logout(request)
	return redirect('/')

# CRUD Pengguna
@login_required
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

@login_required
def detail(req, id):
    pengguna = models.Pengguna.objects.filter(pk=id).first()    
    return render(req, 'detail.html', {
        'data': pengguna,
    })

@login_required
def index(req):
    pengguna = models.Pengguna.objects.all()
    return render(req, "index.html", {
        'data': pengguna
    })

@login_required
def update(req, id):
    if req.POST:
        pengguna = models.Pengguna.objects.filter(pk=id).update(nama=req.POST['nama'], username=req.POST['username'], password=req.POST['password'])
        return redirect('/')

    pengguna = models.Pengguna.objects.filter(pk=id).first()    
    return render(req, 'update.html', {
        'data': pengguna,
    })

@login_required
def delete(req, id):
    models.Pengguna.objects.filter(pk=id).delete()
    return redirect('/')