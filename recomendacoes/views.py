from django.shortcuts import get_object_or_404, render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import Recomendacao, CategoriaRecomendacao
def recomendacoes(request):
    categorias_recomendacao = CategoriaRecomendacao.objects.all()
    
    context = {
        'categorias_recomendacao': categorias_recomendacao
    }
    
    return render(request, 'recomendacoes/recomendacoes.html', context)
@login_required
def toggle_favorito_recomendacao(request, recomendacao_id):
    recomendacao = get_object_or_404(Recomendacao, id=recomendacao_id)
    if request.user in recomendacao.favoritos.all():
        recomendacao.favoritos.remove(request.user)
    else:
        recomendacao.favoritos.add(request.user)    
    return redirect(request.META.get('HTTP_REFERER', 'recomendacoes'))

def lista_por_categoria(request, pk):
    categoria = get_object_or_404(CategoriaRecomendacao, pk=pk)
    itens = Recomendacao.objects.filter(categoria=categoria)
    
    context = {
        'categoria': categoria,
        'recomendacoes': itens
    }
    return render(request, 'recomendacoes/lista_por_categoria.html', context)
    
