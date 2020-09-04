from django.shortcuts import render, redirect
from part.forms import sukucadangForm, pekerjaForm
from part.models import Sukucadang
from part.models import Pekerja

# from Sukucadang

def emp(request): 
    if request.method == "POST":  
        form = sukucadangForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = sukucadangForm()  
    return render(request,'index.html',{'form':form})  
def show(request):
    datas = Sukucadang.objects.all()
    return render(request, "show.html", {
        'datas': datas
    })
def edit(request, id):
    data = Sukucadang.objects.get(id=id)
    return render(request, 'edit.html', {
        'data': data
    })
def update(request, id):
    data = Sukucadang.objects.get(id=id)
    form = sukucadangForm(request.POST, instance = data)
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {
        'data': data
    })  
def destroy(request, id):
    data = Sukucadang.objects.get(id=id)
    data.delete()
    return redirect("/show")

# from Employee

def home(request):
    form = pekerjaForm()
    if request.method == "POST":  
        form = pekerjaForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show_pegawai')  
            except:  
                pass  
    return render(request,'home.html',{'form':form})
def show_pegawai(request):
    datas = Pekerja.objects.all()
    return render(request, "show_pegawai.html", {
        'datas': datas
    })
def edit_pegawai(request, id):
    data = Pekerja.objects.get(id=id)
    return render(request, 'edit_pegawai.html', {
        'data': data
    })
def update_pegawai(request, id):
    data = Pekerja.objects.get(id=id)
    form = pekerjaForm(request.POST, instance = data)
    if form.is_valid():  
        form.save()  
        return redirect("/show_pegawai")  
    return render(request, 'edit_pegawai.html', {
        'data': data
    })  
def destroy_pegawai(request, id):
    data = Pekerja.objects.get(id=id)
    data.delete()
    return redirect("/show_pegawai")

# menu view

def menu(request):
    data = Pekerja.objects.all()
    return render(request, "menu.html", {
        'data': data
    })