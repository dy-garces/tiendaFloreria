from django import forms
from django.contrib.auth.forms import UserCreationForm
from usuarios.models import PerfilUsuario

class CustomUserCreationForm(UserCreationForm):
    pass

class frmPerfilUsuario(forms.ModelForm):
    class Meta:
        model = PerfilUsuario
        fields=["rut","nombre","apellido"
        ,"fecha_nac","direccion","correo","numero"
        ,"comuna","imagen","vendedor","suscrito"]