from django.test import TestCase as DjangoTestCase
from unittest import TestCase
from authors.forms import RegisterForm
from parameterized import parameterized
from django.urls import reverse

class AuthorRegisterFormUnitTest(TestCase):
    @parameterized.expand([
        ('first_name', 'Primeiro Nome'),
        ('last_name', 'Sobrenome'),
        ('username', 'Nome de Usuário'),
        ('email', 'Email'),
        ('password', 'Senha'),
        ('password2', 'Repita sua Senha'),
    ])
    def test_filds_labels(self, field, label):
        form = RegisterForm()
        current_label = form.fields[field].label
        self.assertEqual(current_label, label)

    @parameterized.expand([
        ('first_name', 'Digite aqui seu primeiro nome'),
        ('last_name', 'Digite aqui seu sobrenome'),
        ('username', 'Digite aqui seu nome de usuário'),
        ('email', 'Digite aqui seu email'),
        ('password', 'Digite aqui sua senha'),
        ('password2', 'Repita aqui sua senha'),
    ])
    def test_filds_placehoder(self, field, placeholder):
        form = RegisterForm()
        current_placeholder = form.fields[field].widget.attrs['placeholder']
        self.assertEqual(current_placeholder, placeholder)

    def test_filds_help_text(self):
        form = RegisterForm()
        current_help_text = form.fields['username'].help_text
        self.assertEqual(current_help_text, 'Username deve conter letras, números ou @.+-_ . E seu tamanho entre 4 e 150 caracteres.')


class AuthorRegisterFormIntegrationTest(DjangoTestCase):
    def setUp(self, *args, **kwargs):
        self.form_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'username': 'johndoe',
            'email': 'HdD0g@example.com',
            'password': '12345678aA',
            'password2': '12345678aA',
        }
        return super().setUp(*args, **kwargs)
    
    @parameterized.expand([
        ('first_name', 'Primeiro Nome não pode estar vazio.'),
        ('last_name', 'Sobrenome não pode estar vazio.'),
        ('username', 'Username não pode estar vazio.'),
        ('email', 'Email não pode estar vazio.'),
        ('password', 'Senha não pode estar vazia.'),
        ('password2', 'Repita sua senha não pode estar vazia.'),
    ])
    def test_fields_cannot_be_empty(self, field, msg):
        self.form_data[field] = ''
        url = reverse('authors:register_create')
        response = self.client.post(url, data=self.form_data, follow=True)
        self.assertIn(msg, response.content.decode('utf-8'))
        self.assertIn(msg, response.context['form'].errors.get(field))

    def test_username_field_min_lenght_shoud_be_4(self):
        self.form_data['username'] = 'joh'
        url = reverse('authors:register_create')
        response = self.client.post(url, data=self.form_data, follow=True)
        msg = 'Username deve ter no minimo 4 caracteres.'
        self.assertIn(msg, response.content.decode('utf-8'))
        self.assertIn(msg, response.context['form'].errors.get('username'))

    def test_username_field_max_lenght_shoud_be_150(self):
        self.form_data['username'] = 'A' * 151
        url = reverse('authors:register_create')
        response = self.client.post(url, data=self.form_data, follow=True)
        msg = 'Username deve ter no maximo 150 caracteres.'
        self.assertIn(msg, response.content.decode('utf-8'))
        self.assertIn(msg, response.context['form'].errors.get('username'))

    def test_password_field_is_correct(self):
        self.form_data['password'] = '123abcA'
        self.form_data['password2'] = '123abcA'
        url = reverse('authors:register_create')
        response = self.client.post(url, data=self.form_data, follow=True)
        msg = 'A senha deve ter pelo menos 8 caracteres, uma letra minúscula, uma letra maiúscula e um número.'
        self.assertIn(msg, response.content.decode('utf-8'))
        self.assertIn(msg, response.context['form'].errors.get('password'))

    def test_password_and_password2_are_equal(self):
        self.form_data['password'] = '123abcA'
        self.form_data['password2'] = '123'
        url = reverse('authors:register_create')
        response = self.client.post(url, data=self.form_data, follow=True)
        msg = 'As senhas não coincidem.'
        self.assertIn(msg, response.content.decode('utf-8'))
        self.assertIn(msg, response.context['form'].errors.get('password'))

    def test_send_get_request_to_registration_create_view_returns_404(self):
        url = reverse('authors:register_create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_email_field_must_be_unique(self):
        url = reverse('authors:register_create')
        self.client.post(url, data=self.form_data, follow=True)
        response = self.client.post(url, data=self.form_data, follow=True)

        msg = 'E-mail já existe'
        self.assertIn(msg,response.context['form'].errors.get('email'))
        self.assertIn(msg, response.content.decode('utf-8'))

    def test_author_created_can_login(self):
        url = reverse('authors:register_create')

        self.form_data.update({
            'username': 'johndoe',
            'password': '12345678aA',
            'password2': '12345678aA',
        })

        self.client.post(url, data=self.form_data, follow=True)

        is_authenticated = self.client.login(
            username='johndoe',
            password='12345678aA'
        )

        self.assertTrue(is_authenticated)

