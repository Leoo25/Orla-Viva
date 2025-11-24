from django.shortcuts import get_object_or_404, render
# Create your views here.
from .models import Recomendacao, CategoriaRecomendacao
def recomendacoes(request):
    categorias_recomendacao = CategoriaRecomendacao.objects.all()
    
    context = {
        'categorias_recomendacao': categorias_recomendacao
    }
    
    return render(request, 'recomendacoes/recomendacoes.html', context)

def lista_por_categoria(request, pk):
    categoria = get_object_or_404(CategoriaRecomendacao, pk=pk)
    itens = Recomendacao.objects.filter(categoria=categoria)
    
    context = {
        'categoria': categoria,
        'recomendacoes': itens
    }
    return render(request, 'recomendacoes/lista_por_categoria.html', context)
    
