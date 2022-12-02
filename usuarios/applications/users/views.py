from django.shortcuts import render
#Funcion para enviar email
from django.core.mail import send_mail
from django.urls import reverse_lazy, reverse

#PAra autenticar usuarios en el login de una app
from django.contrib.auth import authenticate, login, logout

#Para redireccionar al usuario
from django.http import HttpResponseRedirect

#Usuario que este logueado
from django.contrib.auth.mixins import LoginRequiredMixin


from django.views.generic import (
    View,
    CreateView
)
from django.views.generic.edit import FormView
from .forms import UserRegisterForm, LoginForm, UpdatePasswordForm, VerificationForm

#Importando manager y modelo
from .models import User

#Importar funciones
from .functions import code_generator

# Create your views here.
class UserRegisterView(FormView):
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    success_url = '/'

    def form_valid(self,form):
        #Generamos el codigo
        codigo = code_generator()

        User.objects.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['email'],
            form.cleaned_data['password1'],
            #como pasa un extra_field
            nombres = form.cleaned_data['nombres'],
            apellidos = form.cleaned_data['apellidos'],
            genero = form.cleaned_data['genero'],
            #codregistro = codigo
        )
        return super(UserRegisterView, self).form_valid(form)
        #Enviar el codigo al email del usuario
        #asunto = 'Confirmacion de E-mail'
        #mensaje = 'Codigo de verificacion: ' + codigo
        #email_remitente = 'juanpmufc9508@gmail.com'
        #
        #send_mail(asunto, mensaje, email_remitente, [form.cleaned_data['email'],])
        #Redirigir a pantalla de validacion
        
        #return HttpResponseRedirect(#Redirige al usuario a otro lado
        #    reverse(
        #        'users_app:user-login'
        #    )
        #)

#Clase que hara el login del usuarios
class LoginUser(FormView):
    template_name = 'users/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home_app:panel')

    def form_valid(self, form):
        user = authenticate( #Aqui verificamos un usuarios que se haya registrado en la base de datos
            username = form.cleaned_data['username'],
            password = form.cleaned_data['password'],
        )
        #hacer el Login para que este activo
        login(self.request, user)
        return super(LoginUser, self).form_valid(form)


#Vista para cerrar sesion
class LogoutView(View):

    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(#Redirige al usuario a otro lado
            reverse(
                'users_app:user-login'
            )
        )

#Vista para actualizar una contraseña
class UpdatePasswordView(LoginRequiredMixin, FormView):
    template_name = 'users/update.html'
    form_class = UpdatePasswordForm
    success_url = reverse_lazy('users_app:user-login')
    login_url = reverse_lazy('users_app:user-login')


    def form_valid(self, form):
        #Verificar que el usuario este activo y luego actualizar
        usuario = self.request.user #Variable que recupera el usuario
        user = authenticate(   #Hacer autenticacion
            username = usuario.username,
            password = form.cleaned_data['password1'],
        )
        #Si la autenticacion es correcta
        if user:
            new_password = form.cleaned_data['password2']
            usuario.set_password(new_password)
            usuario.save()
        logout(self.request)
        return super(UpdatePasswordView, self).form_valid(form)


#Vista de verificacion de codigo
class CodeVerificacionView(FormView):
    template_name = 'users/verification.html'
    form_class = VerificationForm
    success_url = reverse_lazy('users_app:user-login')

    def form_valid(self, form):
        
        return super(CodeVerificacionView, self).form_valid(form)
