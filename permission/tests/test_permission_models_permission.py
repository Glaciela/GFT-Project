from .teste_permission_base import PermissionTestBase, Permission, timezone
from django.core.exceptions import ValidationError
from parameterized import parameterized

class PermissionModelsTest(PermissionTestBase):
    def setUp(self):
        self.permission = self.make_permission()
        return super().setUp()
    
    def make_permission_no_defaults(self):
        permission = Permission(
            slug='slug1',
            location='Local',
            description='Descrição',
            order='Ordem',
            author=self.make_user(username='newauthor'),
            date_search='2025-01-01',    
            reason=self.make_interdiction(name='newreason'),
            date_start=timezone.now(),
            date_end=timezone.now(),      
        )
        permission.full_clean()
        permission.save()   
        return permission

    @parameterized.expand([
        ('location', 65),
        ('description', 65),
        ('order', 65),
    ])
    def test_permission_fields_max_length(self, field, max_length):
        setattr(self.permission, field, 'A' * (max_length + 1))
        with self.assertRaises(ValidationError):
            self.permission.full_clean() 

    def test_permission_is_published_is_false_by_default(self):
        permission = self.make_permission_no_defaults()
        self.assertFalse(permission.is_published, msg='is_published é verdadeiro por padrão')

    def test_permission_string_representation(self):
        self.permission.location = 'newlocation'
        self.permission.full_clean()
        self.permission.save()

        self.assertEqual(str(self.permission), 'Interdição na newlocation solicitado por username')
      
