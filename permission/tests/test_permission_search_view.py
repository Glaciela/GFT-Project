from django.urls import reverse, resolve
from permission import views
from .teste_permission_base import PermissionTestBase

class PermissionSearchViewTest(PermissionTestBase):

    def test_permission_search_uses_correct_view_function(self):
        resolved = resolve(reverse('permission:search'))
        self.assertIs(resolved.func, views.search)

    def test_permission_search_loads_correct_template(self):
        response = self.client.get(reverse('permission:search') + '?q=teste')
        self.assertTemplateUsed(response, 'permission/pages/search.html')

    def test_permission_search_raises_404_if_no_search_term(self):
        url = reverse('permission:search') 
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_permission_search_term_is_on_page_title_and_escaped(self):
        url = reverse('permission:search') + '?q=teste'
        response = self.client.get(url)
        self.assertIn(
            'Busca por &quot;teste&quot;',
            response.content.decode('utf-8')
        )
