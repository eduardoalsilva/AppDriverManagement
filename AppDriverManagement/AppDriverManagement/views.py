from django.shortcuts import render, redirect
from .models import GanhoDiario, GastoCombustivel, AluguelSemanal, Meta
from .forms import GanhoDiarioForm, GastoCombustivelForm, AluguelSemanalForm, MetaForm

def registrar_ganho(request):
    if request.method == 'POST':
        form = GanhoDiarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ganho_diario_list')
    else:
        form = GanhoDiarioForm()
    return render(request, 'registrar_ganho.html', {'form': form})

def registrar_gasto_combustivel(request):
    if request.method == 'POST':
        form = GastoCombustivelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gasto_combustivel_list')
    else:
        form = GastoCombustivelForm()
    return render(request, 'registrar_gasto_combustivel.html', {'form': form})

def registrar_aluguel_semanal(request):
    if request.method == 'POST':
        form = AluguelSemanalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('aluguel_semanal_list')
    else:
        form = AluguelSemanalForm()
    return render(request, 'registrar_aluguel_semanal.html', {'form': form})

def definir_meta(request):
    if request.method == 'POST':
        form = MetaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('meta_list')
    else:
        form = MetaForm()
    return render(request, 'definir_meta.html', {'form': form})

def ganho_diario_list(request):
    ganhos = GanhoDiario.objects.all()
    return render(request, 'ganho_diario_list.html', {'ganhos': ganhos})

def gasto_combustivel_list(request):
    gastos = GastoCombustivel.objects.all()
    return render(request, 'gasto_combustivel_list.html', {'gastos': gastos})

def aluguel_semanal_list(request):
    alugueis = AluguelSemanal.objects.all()
    return render(request, 'aluguel_semanal_list.html', {'alugueis': alugueis})

def meta_list(request):
    metas = Meta.objects.all()
    return render(request, 'meta_list.html', {'metas': metas})