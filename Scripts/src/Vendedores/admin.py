from django.contrib import admin
from django.conf import settings

# Register your models here.
from Vendedores.models import Trabajadores

class adminTrabajadores(admin.ModelAdmin):
	list_display = ['nombre', 'apellidos']
	class Meta:
		model = Trabajadores

admin.site.register(Trabajadores, adminTrabajadores)


# Customización de la interfaz de admin
admin.site.site_header = settings.ADMIN_SITE_HEADER
