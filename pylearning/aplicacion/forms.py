from django import forms
from . models import Usuario

class usuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = {
            'nombre_usuario',
            'nombre',
            'apellido',
            'email',
            'contrasena'
        }