from django import forms 
from harga.models import Harga

class hargaForm(forms.ModelForm):
    class Meta:
        model = Harga
        fields = "__all__"  