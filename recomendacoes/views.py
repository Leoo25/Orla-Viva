from django.shortcuts import render

# Create your views here.
def recomendacoes(request):
    return render(request,'recomendacoes/recomendacoes.html')
    
