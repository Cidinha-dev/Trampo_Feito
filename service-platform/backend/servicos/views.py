from django.shortcuts import render
from .models import Servico

def lista_servicos(request):
    servicos = Servico.objects.all()
    return render(request, 'servicos/lista_servicos.html', {'servicos': servicos})

def buscar_servicos(request):
    query = request.GET.get('q', '')
    resultados = Servico.objects.filter(nome__icontains=query) if query else Servico.objects.all()
    return render(request, 'servicos/buscar_servicos.html', {'resultados': resultados, 'query': query})
