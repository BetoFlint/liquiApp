# forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm

#class LoginForm(AuthenticationForm):
#    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de usuario'}))
    #password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}))
#    pass

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={
            'class': 'inputs.css',
            'autocomplete': 'off',
            'required': 'required',  # Asegura que el campo sea requerido
            'type': 'text'  # Aunque es el valor por defecto para TextInput
        })
        self.fields['password'].widget = forms.PasswordInput(attrs={
            'autocomplete': 'off',
            'required': 'required'  # Asegura que el campo sea requerido
            
        })
