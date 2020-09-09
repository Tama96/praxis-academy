from django.shortcuts import render, redirect
from pekerja.forms import pekerjaForm
from pekerja.models import Pekerja
# Create your views here.

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