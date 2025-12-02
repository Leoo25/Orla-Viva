from django.shortcuts import render, redirect
from .forms import ContatoForm
from django.contrib import messages
from .models import Contato

# Create your views here.


from django.shortcuts import render
from .forms import ContatoForm

def contato(request):
    sucesso = False

    if request.method == "POST":
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save()
            sucesso = True
            form = ContatoForm() 
    else:
        form = ContatoForm()

    return render(request, 'contato/contato.html', {
        'form_contato': form,
        'sucesso': sucesso
    })

def lista_mensagens(request):
    mensagens_contato = Contato.objects.all()
    
    context = {
        'mensagens_contato': mensagens_contato,
    }
    return render(request, 'contato/mensagens.html', context)





