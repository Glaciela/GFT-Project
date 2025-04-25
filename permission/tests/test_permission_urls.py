from django.test import TestCase
from django.urls import reverse
from permission import views

# Create your tests here.
class PermissionURLsTest(TestCase):
    def test_permission_home_urls_is_correct(self):
        home_url = reverse('permission:home')
        self.assertEqual(home_url, '/')

    def test_permission_interdiction_urls_is_correct(self):
        url = reverse('permission:interdiction', kwargs={'interdiction_id': 1})
        self.assertEqual(url, '/permissao/interdiction/1/')

    def test_permission_permission_urls_is_correct(self):
        url = reverse('permission:permission', kwargs={'id': 1})
        self.assertEqual(url, '/permissao/1/')

    def test_permission_search_urls_is_correct(self):
        url = reverse('permission:search')
        self.assertEqual(url, '/permissao/search/')
