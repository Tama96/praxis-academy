from django import forms 
from pekerja.models import Pekerja

class pekerjaForm(forms.ModelForm):
    class Meta:
        model = Pekerja
        fields = "__all__"  