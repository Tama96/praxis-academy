from django import forms 
from part.models import Sukucadang,Pekerja

class sukucadangForm(forms.ModelForm): 
    class Meta:  
        model = Sukucadang  
        fields = "__all__"

class pekerjaForm(forms.ModelForm):
    class Meta:
        model = Pekerja
        fields = "__all__"  