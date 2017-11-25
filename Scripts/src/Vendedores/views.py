from django.shortcuts import render

# Create your views here.
from .models import Trabajadores

def home(request):
	query = Trabajadores.objects.all()
	contexto = {
			"lista_vendedores":query
		}
	return render(request, 'Vendedores/showVendors.html', contexto)
