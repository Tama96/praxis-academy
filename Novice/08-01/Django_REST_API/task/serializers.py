from rest_framework import serializers
from .models import Pekerjaan

class PekerjaanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pekerjaan
        fields = ('id', 'nama', 'motto')