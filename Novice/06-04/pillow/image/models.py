from django.db import models
from django.core.files import File
from django.conf import settings
import PIL.Image
import glob
import os.path

# Create your models here.

def upload_location(instance, filename, **kwargs):
    file_path = 'images/{filename}'.format(filename=filename)
    return file_path

class Image(models.Model):
    image = models.ImageField(upload_to='images', null=False, blank=True)

    def save(self,force_insert=False, force_update=False, using=None,*args, **kwargs):
        super(Image, self).save(*args, **kwargs)
        if self.image:
            image = self.image
            if image.size > 0.3*1024*1024: #if size greater than 300kb then it will send to compress image function
                self.compress_image(image)
                print(image)
    

    def compress_image(self, uploadedImage):
        im = PIL.Image.open("{}{}".format(settings.MEDIA_ROOT,uploadedImage))
        #for (i,im) in enumerate(glob.glob('settings.MEDIA_ROOT,uploadedImage')):
            #print (im)
        if im.mode != 'RGB':
            im = im.convert('RGB')
        new_image = im.resize((round(im.size[0]*0.5), round(im.size[1]*0.5)))
        new_image.save('{}{}'.format(settings.MEDIA_ROOT,uploadedImage))
        # self.image = "{}{}".format(settings.MEDIA_ROOT,uploadedImage)
    
    def __str__(self):
        return self.title
   
    class Meta:  
        db_table = "myapp_image"