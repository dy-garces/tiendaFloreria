from django.forms import ModelForm
from .models import DireccionEnvio

class DireccionEnvioForms(ModelForm):
    class Meta:
        model = DireccionEnvio
        fields = [ 'envio1'  , 'ciudad' , 'region']
        labels = {
            'envio1': 'Direccion 1',
        }