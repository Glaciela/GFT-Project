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
        error_messages={'required': 'Repita sua senha não pode estar vazia.'},
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
        #labels = {
            #'first_name': 'Primeiro Nome',
            #'last_name': 'Sobrenome',
            # 'username': 'Nome de Usuário',
            #'email': 'Email',
            #'password': 'Senha',
        #}
        #widgets = {
            #'first_name': forms.TextInput(attrs={'placeholder': 'Digite aqui seu primeiro nome'}),
            #'last_name': forms.TextInput(attrs={'placeholder': 'Digite aqui seu sobrenome'}),
            # 'username': forms.TextInput(attrs={'placeholder': 'Digite aqui seu nome de usuário'}),
            #'email': forms.EmailInput(attrs={'placeholder': 'Digite aqui seu email'}),
            #'password': forms.PasswordInput(attrs={'placeholder': 'Digite aqui sua senha'}),
        #}

    first_name = forms.CharField(
        error_messages={'required': 'Primeiro Nome não pode estar vazio.'},
        widget=forms.TextInput(attrs={'placeholder': 'Digite aqui seu primeiro nome'}),
        label='Primeiro Nome',
    )

    last_name = forms.CharField(
        error_messages={'required': 'Sobrenome não pode estar vazio.'},
        widget=forms.TextInput(attrs={'placeholder': 'Digite aqui seu sobrenome'}),
        label='Sobrenome',
    )

    username = forms.CharField(
        error_messages={'required': 'Username não pode estar vazio.',
                        'min_length': 'Username deve ter no minimo 4 caracteres.',
                        'max_length': 'Username deve ter no maximo 150 caracteres.',
                        },
        widget=forms.TextInput(attrs={'placeholder': 'Digite aqui seu nome de usuário'}),
        help_text='Username deve conter letras, números ou @.+-_ . E seu tamanho entre 4 e 150 caracteres.',
        label='Nome de Usuário',
        min_length=4,
        max_length=150,
    )

    email = forms.EmailField(
        error_messages={'required': 'Email não pode estar vazio.'},
        widget=forms.EmailInput(attrs={'placeholder': 'Digite aqui seu email'}),
        label='Email',
    )

    password = forms.CharField(
        error_messages={'required': 'Senha não pode estar vazia.'},
        widget=forms.PasswordInput(attrs={'placeholder': 'Digite aqui sua senha'}),
        label='Senha',
    )

    
    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if not password or not password2:
                raise forms.ValidationError({
                    "password": ''
                })

        elif password and password2 and password != password2:
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