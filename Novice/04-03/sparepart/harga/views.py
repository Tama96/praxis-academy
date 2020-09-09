from django.shortcuts import render, redirect
from harga.forms import hargaForm
from harga.models import Harga

# Create your views here.

# from harga

def home_harga(request):
    form = hargaForm()
    if request.method == "POST":  
        form = hargaForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show_harga')  
            except:  
                pass  
    return render(request,'home_harga.html',{
        'form':form
    })
def show_harga(request):
    datas = Harga.objects.all()
    return render(request, "show_harga.html", {
        'datas': datas
    })
def edit_harga(request, id):
    data = Harga.objects.get(id=id)
    return render(request, 'edit_harga.html', {
        'data': data
    })
def update_harga(request, id):
    data = Harga.objects.get(id=id)
    form = hargaForm(request.POST, instance = data)
    if form.is_valid():  
        form.save()  
        return redirect('/show_harga')  
    return render(request, 'edit_harga.html', {
        'data': data
    })  
def destroy_harga(request, id):
    data = Harga.objects.get(id=id)
    data.delete()
    return redirect('/show_harga')