from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    password2 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'placeholder': 'Repita aqui sua senha'}),
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
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'username': 'Username',
            'email': 'Email Address',
            'password': 'Password',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Digite aqui seu primeiro nome'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Digite aqui seu ultimo sobrenome'}),
            'username': forms.TextInput(attrs={'placeholder': 'Digite aqui seu nome de usuário'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Digite aqui seu email'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Digite aqui sua senha'}),
        }
