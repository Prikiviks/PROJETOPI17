# core/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Filme, Critica
from .forms import FilmeForm

def index(request):
    filmes_recent = Filme.objects.order_by('-data_lancamento')[:5]
    criticas_populares = Critica.objects.order_by('-data_criacao')[:5]
    context = {
        'filmes_recent': filmes_recent,
        'criticas_populares': criticas_populares,
    }
    return render(request, 'index.html', context)

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'registro.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def perfil(request):
    return render(request, 'perfil.html')

@login_required
def lista_filmes(request):
    filmes = Filme.objects.all()
    return render(request, 'lista_filmes.html', {'filmes': filmes})

# src/core/views.py
from django.shortcuts import render, get_object_or_404
from .models import Filme

def detalhe_filme(request, filme_id):
    filme = get_object_or_404(Filme, pk=filme_id)
    return render(request, 'filme_detalhes.html', {'filme': filme})

@login_required
def adicionar_filme(request):
    if request.method == 'POST':
        form = FilmeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_filmes')
    else:
        form = FilmeForm()
    return render(request, 'form_filme.html', {'form': form})

@login_required
def editar_filme(request, filme_id):
    filme = get_object_or_404(Filme, id=filme_id)
    if request.method == 'POST':
        form = FilmeForm(request.POST, request.FILES, instance=filme)
        if form.is_valid():
            form.save()
            return redirect('detalhe_filme', filme_id=filme.id)
    else:
        form = FilmeForm(instance=filme)
    return render(request, 'form_filme.html', {'form': form})

@login_required
def excluir_filme(request, filme_id):
    filme = get_object_or_404(Filme, id=filme_id)
    filme.delete()
    return redirect('lista_filmes')