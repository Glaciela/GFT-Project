from .teste_permission_base import PermissionTestBase
from django.core.exceptions import ValidationError

class PermissionInterdictionModelTest(PermissionTestBase):
    def setUp(self):
        self.interdiction = self.make_interdiction(name='newinterdição')
        return super().setUp()
    
    def test_permission_interdiction_string_representation_is_name_field(self):
        self.assertEqual(str(self.interdiction), self.interdiction.name) 

    def test_permission_interdiction_model_name_max_length_is_65_chars(self):
        self.interdiction.name = 'A' * 66
        with self.assertRaises(ValidationError):
            self.interdiction.full_clean()
