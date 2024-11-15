from django import forms
from .models import Techpro

class formTechpro(forms.ModelForm):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('en_progreso', 'En Progreso'),
        ('completado', 'Completado'),
        ('cancelado', 'Cancelado'),
    ]
    
    Estado = forms.ChoiceField(choices=ESTADO_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))     

    class Meta:
        model = Techpro 
        fields = ['Cliente', 'Tecnico', 'Fecha_Solicitud', 'Fecha_Finalizacion', 'Estado', 'Descripcion']
        widgets = {
            'CLiente': forms.TextInput(attrs={'class': 'form-control'}),
            'Tecnico': forms.TextInput(attrs={'class': 'form-control'}),
            'Fecha_Solicitud': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'Fecha_Finalizacion': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'Descripcion': forms.Textarea(attrs={'class': 'form-control'}),
        }