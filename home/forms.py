from django import forms

estilo_defecto = {
        'class':'uk-input'
    }

class LoginForm(forms.Form):
    usuario = forms.CharField(label='Nombre de usuario', max_length=30)
    clave = forms.CharField(label='Contraseña')

    usuario.widget = forms.TextInput(attrs=estilo_defecto)
    clave.widget = forms.PasswordInput(attrs=estilo_defecto)
    
class RegistroForm(forms.Form):
    usuario = forms.CharField(label='Nombre de usuario', max_length=30)
    clave = forms.CharField(label='Contraseña')
    confirmacion = forms.CharField(label='Confirmación')

    usuario.widget = forms.TextInput(attrs=estilo_defecto)
    clave.widget = forms.PasswordInput(attrs=estilo_defecto)
    confirmacion.widget = forms.PasswordInput(attrs=estilo_defecto)

class ComentarioForm(forms.Form):
    comentario = forms.CharField(label='Comentario', max_length=200)

    comentario.widget = forms.Textarea(attrs={'class':'uk-textarea uk-form-small'})