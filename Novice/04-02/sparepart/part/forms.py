from django import forms 
from part.models import Sukucadang,Pekerja,Harga

class sukucadangForm(forms.ModelForm): 
    class Meta:  
        model = Sukucadang  
        fields = "__all__"

class pekerjaForm(forms.ModelForm):
    class Meta:
        model = Pekerja
        fields = "__all__"  

class hargaForm(forms.ModelForm):
    class Meta:
        model = Harga
        fields = "__all__"  