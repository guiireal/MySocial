from .models import Perfil
from django.shortcuts import render, redirect


def index(request):
    users = Perfil.objects.all()
    return render(request, 'perfis/index.html', 
        { 
            'usuarios' : users , 
            'perfil_logado' : get_perfil_logado(request)
        })

def exibir(request, perfil_id):
    perfil = Perfil.objects.get(id = perfil_id)
    return render(request, 'perfis/perfil.html', 
        { 
            'perfil' : perfil ,
            'perfil_logado' : get_perfil_logado(request)
        })

''' REALIZANDO CONVITE DE CONEXÃO COM OUTRO USUARIO '''
def convidar(request, perfil_id):
    perfil_convite = Perfil.objects.get(id=perfil_id)
    perfil_logado = get_perfil_logado(request)
    perfil_logado.convidar(perfil_convite) 
    return redirect('index')


''' SIMULANDO USUARIO LOGADO PARA TESTES DE CONVITES '''
def get_perfil_logado(request):
    return Perfil.objects.get(id=3)

