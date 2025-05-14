from django.urls import reverse, resolve
from permission import views
from .teste_permission_base import PermissionTestBase
from unittest.mock import patch

class PermissionHomeViewTest(PermissionTestBase):

    def test_permission_home_view_funcion_is_correct(self):
        view = resolve(reverse('permission:home'))
        self.assertEqual(view.func, views.home)

    def test_permission_home_view_returns_status_code_200_OK(self):
        response = self.client.get(reverse('permission:home'))
        self.assertEqual(response.status_code, 200)

    def test_permission_home_view_loads_correct_template(self):
        response = self.client.get(reverse('permission:home'))
        self.assertTemplateUsed(response, 'permission/pages/home.html')

    def test_recipe_home_template_shows_no_permission_found_if_no_recipes(self):
        response = self.client.get(reverse('permission:home'))
        self.assertIn(
             '<h1>Não existem permissões⚠️</h1>',
             response.content.decode('utf-8')
        )
        #Função para forcar o teste a falhar
        #self.fail('Falhou!')

    def test_permission_home_templates_loads_permissions(self):

        # É necessário pelo menos uma permissão para executar o teste
        self.make_permission(reason_data={'name': 'Evento'})

        response = self.client.get(reverse('permission:home'))
        content = response.content.decode('utf-8')
        response_context_permissions = response.context['permissions']
        self.assertEqual(len(response_context_permissions), 1)
        self.assertIn('Ordem', content)
        self.assertIn('Local', content)
        self.assertIn('Descrição', content)
        self.assertIn('Evento', content)

    def test_permission_home_templates_dont_loads_permissions_not_published(self):

        # É necessário pelo menos uma permissão para executar o teste
        self.make_permission(authorized=False)

        response = self.client.get(reverse('permission:home'))

        self.assertIn(
             '<h1>Não existem permissões⚠️</h1>',
             response.content.decode('utf-8')
        )
    # @patch('permission.views.PER_PAGE', new=2)
    def test_permission_home_is_paginated(self):
        for i  in range(9):
            kwargs = {'slug': f'r{i}', 'author_data': {'username': f'u{i}'}}
            self.make_permission(**kwargs)

        with patch('permission.views.PER_PAGE', new=4):
            response = self.client.get(reverse('permission:home'))
            permissions = response.context['permissions']
            paginator = permissions.paginator
            self.assertEqual(paginator.num_pages, 3)
            self.assertEqual(len(paginator.get_page(1)), 4)
            self.assertEqual(len(paginator.get_page(3)), 1)
      
