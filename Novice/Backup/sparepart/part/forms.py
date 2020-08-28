from django import forms 
from part.models import Sukucadang

class sukucadangForm(forms.ModelForm): 
    class Meta:  
        model = Sukucadang  
        fields = "__all__"  