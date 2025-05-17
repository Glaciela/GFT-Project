from django import forms
from django.contrib.auth.models import User
import re

# def strong_password(password):
#     regex = re.compile(r'^(?=.*[A-Za-z])(?=.[0-9]).{8,}$')
#     if not regex.match(password):
#         raise forms.ValidationError(
#             'A senha deve ter pelo menos 8 caracteres, '
#             'uma letra minúscula, uma letra maiúscula '
#             'e um número.'
#         )
class RegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    password2 = forms.CharField(
        label='Repita sua Senha',
        widget=forms.PasswordInput(attrs={'placeholder': 'Repita aqui sua senha'}),
        # validators=[strong_password],
    )
    class Meta:
        model = User
        # fields = '__all__'
        # exclude = ['first_name', 'last_name']
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
        ]
        labels = {
            'first_name': 'Primeiro Nome',
            'last_name': 'Sobrenome',
            'username': 'Nome de Usuário',
            'email': 'Email',
            'password': 'Senha',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Digite aqui seu primeiro nome'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Digite aqui seu sobrenome'}),
            'username': forms.TextInput(attrs={'placeholder': 'Digite aqui seu nome de usuário'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Digite aqui seu email'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Digite aqui sua senha'}),
        }
    
    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password and password2 and password != password2:
            raise forms.ValidationError({
                "password": 'As senhas não coincidem.'
                })
        
        regex = re.compile(r'^(?=.*[A-Za-z])(?=.[0-9]).{8,}$')
        if not regex.match(password):
            raise forms.ValidationError({
            "password":
            'A senha deve ter pelo menos 8 caracteres, '
            'uma letra minúscula, uma letra maiúscula '
            'e um número.'
            })

        return cleaned_data