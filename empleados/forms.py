from django import forms
from .models import Empleados

class formEmpleados(forms.ModelForm):
    class Meta:
        model = Empleados
        fields = ['Nombre', 'Apellido', 'Cedula', 'Fecha_Nacimiento', 'Edad', 'Cargo', 'email'
                  ]