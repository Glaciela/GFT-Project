from django.contrib import admin
from .models import Interdiction, Permission

# Register your models here.
class InterdictionAdmin(admin.ModelAdmin):
    ...
@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    ...

admin.site.register(Interdiction, InterdictionAdmin)