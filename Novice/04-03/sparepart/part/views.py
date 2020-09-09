from django.shortcuts import render, redirect
from part.forms import sukucadangForm
from part.models import Sukucadang

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

# menu view

def menu(request):
    data = Sukucadang.objects.all()
    return render(request, "menu.html", {
        'data': data
    })

