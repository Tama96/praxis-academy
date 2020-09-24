from django.shortcuts import render, redirect
from image.forms import ImageForm
from image.models import Image
from django.views.generic.edit import FormView

class FileFieldView(FormView):
    form_class = ImageForm
    template_name = 'index.html'  
    success_url = '' 

def index(request, *args, **kwargs):
    form = ImageForm()
    if request.method == 'POST':
        files = request.FILES.getlist('image')
        images = []
        for file in files:
            images.append(Image.objects.create(image=file))
        return render(request, 'index.html', {'form': form, 'images': images})
    return render(request, 'index.html', {'form': form})

