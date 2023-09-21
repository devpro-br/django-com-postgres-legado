from django.contrib import admin

from devpro.base.models import Curso


# Register your models here.

@admin.register(Curso)
class CursosAdmin(admin.ModelAdmin):
    list_display = 'id name created_at updated_at'.split()
