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
    def test_permission_search_can_find_permission_by_location(self):
        location1 = 'Av Afonso Pena, 1000'
        location2 = 'Av Afonso Pena, 2000'

        permission1 = self.make_permission(
            location=location1,
            slug='slug1',
            author_data={'username': 'newauthor1'},
        )

        pemission2 = self.make_permission(
            location=location2,
            slug='slug2',
            author_data={'username': 'newauthor2'},
        )

        search_url = reverse('permission:search')
        response1 = self.client.get(f'{search_url}?q={location1}')
        response2 = self.client.get(f'{search_url}?q={location2}')
        response_both = self.client.get(f'{search_url}?q=Av Afonso Pena')

        self.assertIn(permission1, response1.context['permissions'])
        self.assertNotIn(pemission2, response1.context['permissions'])
        self.assertIn(pemission2, response2.context['permissions'])
        self.assertNotIn(permission1, response2.context['permissions'])
        self.assertIn(permission1, response_both.context['permissions'])
        self.assertIn(pemission2, response_both.context['permissions'])
        

