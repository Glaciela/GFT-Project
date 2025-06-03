from django import forms

class LoginForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Digite aqui seu nome de usuário'}),
        label='Nome de Usuário',
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Digite aqui sua senha'}),
        label='Senha',
    )