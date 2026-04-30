from django import forms
from .models import Calificacion
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'correo@ejemplo.com'}))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Aplicamos la clase form-control a todos los campos para mantener el diseño premium
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

class CalificacionForm(forms.ModelForm):
    class Meta:
        model = Calificacion
        fields = ['nombre_estudiante', 'identificacion', 'asignatura', 'nota1', 'nota2', 'nota3']
        widgets = {
            'nombre_estudiante': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre Completo'}),
            'identificacion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Identificación'}),
            'asignatura': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Asignatura'}),
            'nota1': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': '0', 'max': '5'}),
            'nota2': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': '0', 'max': '5'}),
            'nota3': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': '0', 'max': '5'}),
        }

class UsernameRecoveryForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo Electrónico'}),
        label="Correo Electrónico"
    )
