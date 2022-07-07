from django import forms
from django.contrib.auth.forms import UserCreationForm
from usuarios.models import PerfilUsuario
from tiendaFloreria.Rut import validarRut

class CustomUserCreationForm(UserCreationForm):
    pass

class frmPerfilUsuario(forms.ModelForm):
    class Meta:
        model = PerfilUsuario
        fields=["rut","nombre","apellido"
        ,"fecha_nac","direccion","correo","numero"
        ,"comuna","imagen","vendedor"]
    def clean(self):
        super(frmPerfilUsuario, self).clean()
        ruts = self.cleaned_data.get('rut')
        if  validarRut(str(ruts)) == False:
            self.errors['rut'] = self.error_class(['Rut Invalido'])
        return self.cleaned_data