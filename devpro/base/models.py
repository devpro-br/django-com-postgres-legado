from django.db import models

class Curso(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    a = models.CharField(max_length=255, null=True, default='', blank='')

    class Meta:
        managed = True
        db_table = 'cursos'

