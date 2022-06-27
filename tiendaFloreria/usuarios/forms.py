from cProfile import label
from dataclasses import field
from django import forms
from .models import Comuna, Region

class FormularioRegion(forms.ModelForm):
    class Meta:
        model = Region
        fields = ["nombre"]
        

class FormularioComuna(forms.ModelForm):
    class Meta:
        model = Comuna
        fields = ["nombre","region"]
        