from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Interdiction(models.Model):
    name = models.CharField(max_length=65)

    def __str__(self):
        return self.name

class Permission(models.Model):
    slug = models.SlugField(unique=True)
    location = models.CharField(max_length=65)
    lat = models.CharField(max_length=15, null=True)
    lon = models.CharField(max_length=15, null=True)
    description = models.CharField(max_length=65)
    order = models.CharField(max_length=65)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date_register = models.DateField()
    reason = models.ForeignKey(
        Interdiction, on_delete=models.SET_NULL, null=True,
        blank=True, default=None
        )
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    authorized = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.reason} na {self.location} solicitado por {self.author}'