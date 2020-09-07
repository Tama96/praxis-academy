from django import forms 
from list.models import Tugas

class listForm(forms.ModelForm):
    class Meta:  
        model = Tugas
        fields = "__all__"