from django.shortcuts import render, redirect
 
from image.forms import ImageForm
 
def index(request):
    ImageForm(request.POST, request.FILES)
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.cleaned_data
            # print (dir(form))
            return render(request, 'index.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'index.html', {'form': form})

