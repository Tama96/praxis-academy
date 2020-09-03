from django.shortcuts import render, redirect
from part.forms import sukucadangForm
from part.models import Sukucadang
from part.models import Employee

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
    if request.method == "POST":  
        form = pekerjaForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show2')  
            except:  
                pass  
    else:  
        form = sukucadangForm()  
    return render(request,'home.html',{'form':form})
def show2(request):
    datas = Pekerja.objects.all()
    return render(request, "show2.html", {
        'datas': datas
    })
def edit2(request, id):
    data = Pekerja.objects.get(id=id)
    return render(request, 'edit2.html', {
        'data': data
    })
def update2(request, id):
    data = Pekerja.objects.get(id=id)
    form = pekerjaForm(request.POST, instance = data)
    if form.is_valid():  
        form.save()  
        return redirect("/show2")  
    return render(request, 'edit2.html', {
        'data': data
    })  
def destroy2(request, id):
    data = Pekerja.objects.get(id=id)
    data.delete()
    return redirect("/show2")