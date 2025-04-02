from django.urls import reverse, resolve
from permission import views
from .teste_permission_base import PermissionTestBase

class PermissionViewsTest(PermissionTestBase):

    ################################### TESTES HOME ###################################
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
        self.assertIn('Descritivo', content)
        self.assertIn('Evento', content)

################################### TESTES INTERDIÇÕES ###################################
    def test_permission_interdiction_view_funcion_is_correct(self):
        view = resolve(
            reverse('permission:interdiction', kwargs={'interdiction_id': 1000})
        )
        self.assertEqual(view.func, views.interdiction)

    def test_permission_interdiction_view_returns_404_if_no_permissions_found(self):
        response = self.client.get(
            reverse('permission:interdiction', kwargs={'interdiction_id': 1000})
            )
        self.assertEqual(response.status_code, 404)

    def test_permission_interdiction_template_loads_permissions(self):
        new_location = 'R da Paz'
        # É necessário pelo menos uma permissão para executar o teste
        self.make_permission(location=new_location)

        response = self.client.get(reverse('permission:interdiction', args=(1,)))
        content = response.content.decode('utf-8')

        self.assertIn(new_location, content)

################################### TESTES PERMISSÕES ###################################
    def test_permission_detail_view_funcion_is_correct(self):
        view = resolve(
        reverse('permission:permission', kwargs={'id': 1000})
        )
        self.assertEqual(view.func, views.permissionview)

    def test_permission_detail_view_returns_404_if_no_permissions_found(self):
        response = self.client.get(
            reverse('permission:permission', kwargs={'id': 1000})
            )
        self.assertEqual(response.status_code, 404)

    def test_permission_detail_template_loads_the_correct_permission(self):
        new_location = 'Uma permissao'
        # É necessário pelo menos uma permissão para executar o teste
        self.make_permission(location=new_location)

        response = self.client.get(
            reverse(
                'permission:permission', 
                kwargs={'id': 1}
                ))
        content = response.content.decode('utf-8')

        self.assertIn(new_location, content)