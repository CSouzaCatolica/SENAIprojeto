from django.shortcuts import render, redirect
from app_home.models import Cargos, Usuario, Item, Estoque, Emprestimo


# Create your views here.
def dev(request):
    return render(request, 'app_home/pages/home.html')


def home(request):
    return render(request, 'app_home/global/index.html', context={'usuario': request.session.get('usuario') or None
                                                       , 'cargo': request.session.get('id_cargo') or None
                                                       , 'authorized': request.session.get('authorized') or False})


def login(request):
    if request.method == 'GET':
        if 'authorized' in request.session and request.session['authorized'] == True:
            return redirect('/')
        return render(request, 'app_home/pages/login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if Usuario.objects.filter(nome=username).exists():
            if Usuario.checkSenha(password, Usuario.objects.get(nome=username).senha):
                request.session['usuario'] = username
                request.session['id'] = Usuario.objects.get(nome=username).id
                request.session['id_cargo'] = Usuario.objects.get(nome=username).cargo.id
                request.session['authorized'] = True
                return redirect('/')
            else:
                print("Senha incorreta") # senha incorreta TODO
                return redirect('/login')
        else:
            print("Usuário não encontrado") # usuário não encontrado TODO
            return redirect('/login')