from django.test import TestCase
from permission.models import Permission, Interdiction, User
from django.utils import timezone
class PermissionTestBase(TestCase):
    # executado antes de chamar os métodos de testes
    def setUp(self) -> None:
        return super().setUp()
    
    # executado depois de chamar os métodos de testes
    # def tearDown(self):
    #     ...
    def make_interdiction(self, name='Interdição'):
        return Interdiction.objects.create(name=name)
    
    def make_user(
            self,
            username='username',
            first_name='Nome',
            last_name='Sobrenome',
            password='123456',
            email='a@b.com',
            ):
        return User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password,
            email=email,
            )
    def make_permission(
        self,
        slug='slug',
        location='Local',
        description='Descrição',
        order='Ordem',
        author_data=None,
        date_search='2025-01-01',    
        reason_data=None,
        date_start=timezone.now(),
        date_end=timezone.now(),
        is_published=True,
        ):  
        
        if author_data is None:
            author_data = {}

        if reason_data is None:
            reason_data = {}

        return Permission.objects.create(
            slug=slug,
            location=location,
            description=description,
            order=order,
            author=self.make_user(**author_data),
            date_search=date_search,
            reason=self.make_interdiction(**reason_data),
            date_start=date_start,
            date_end=date_end,
            is_published=is_published,
        )