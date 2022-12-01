from django import forms

#Para validacion de usuarios
from django.contrib.auth import authenticate

from .models import User

class UserRegisterForm(forms.ModelForm):

    password1 = forms.CharField(
        label = 'Contraseña',
        required= True,
        widget= forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña'
            }
        )
    )

    password2 = forms.CharField(
        label = 'Contraseña',
        required= True,
        widget= forms.PasswordInput(
            attrs={
                'placeholder': 'Repetir Contraseña'
            }
        )
    )

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'nombres',
            'apellidos',
            'genero'
        )

    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            self.add_error('password2', 'Las contraseñas no coinciden')#A que atributo pintara el error en la vista


class LoginForm(forms.Form):

    username = forms.CharField(
        label = 'Username',
        required= True,
        widget= forms.TextInput(
            attrs={
                'placeholder': 'Username',
                'style': '{ margin: 10px }'
            }
        )
    )

    password = forms.CharField(
        label = 'Contraseña',
        required= True,
        widget= forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña'
            }
        )
    )
    #Validacion de datos en el login
    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        #verificar que los datos son los correctos para hacer el login
        if not authenticate(username=username, password=password):
            raise forms.ValidationError('Los datos del usuarios son incorrectos')
        
        return self.cleaned_data


class UpdatePasswordForm(forms.Form):
    
    password1 = forms.CharField(
        label = 'Contraseña',
        required= True,
        widget= forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña actual'
            }
        )
    )

    password2 = forms.CharField(
        label = 'Contraseña',
        required= True,
        widget= forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña nueva'
            }
        )
    )