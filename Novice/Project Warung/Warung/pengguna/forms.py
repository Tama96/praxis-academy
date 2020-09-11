from django.forms import ModelForm
from . import models

class penggunaForm(ModelForm):
    class Meta:
        model = models.Pengguna
        exclude = []