from __future__ import unicode_literals

from django.db import models


class Trabajadores(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='NOMBRE', max_length=50)  # Field name made lowercase.
    apellidos = models.CharField(db_column='APELLIDOS', max_length=100)  # Field name made lowercase.

    def __str__(self):
    	return self.nombre

    class Meta:
        managed = True
        db_table = 'vendedores'
        verbose_name_plural = 'Trabajadores'

