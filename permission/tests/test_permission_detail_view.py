from django.urls import reverse, resolve
from permission import views
from .teste_permission_base import PermissionTestBase

class PermissionDetailViewTest(PermissionTestBase):

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
        new_location = 'Rua 14 de julho'
        # É necessário pelo menos uma permissão para executar o teste
        self.make_permission(location=new_location)

        response = self.client.get(
            reverse(
                'permission:permission', 
                kwargs={'id': 1}
                ))
        content = response.content.decode('utf-8')

        self.assertIn(new_location, content)

    def test_permission_detail_templates_dont_loads_permissions_not_published(self):

        # É necessário pelo menos uma permissão para executar o teste
        permission = self.make_permission(authorized=False)

        response = self.client.get(
            reverse('permission:permission', kwargs={'id': permission.id})
            )

        self.assertEqual(response.status_code, 404)