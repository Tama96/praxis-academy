from django import forms
from list.models import Tugas

class listForm (forms.ModelForm):
    deskripsi = forms.CharField(label='deskripsi', max_length=100)
    class Meta:
        model = Tugas
        fields = "__all__"