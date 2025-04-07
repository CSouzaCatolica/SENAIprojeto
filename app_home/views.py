import os, hashlib, binascii
from django.shortcuts import render, redirect
from app_home.models import Cargos, Usuario, Item, Estoque, Emprestimo

# senha com salt + hash
def codSenha(senha: str) -> str:
    salt = os.urandom(32)
    hash_bytes = hashlib.pbkdf2_hmac('sha256', senha.encode(), salt, 100_000)
    
    salt_hex = binascii.hexlify(salt).decode()
    hash_hex = binascii.hexlify(hash_bytes).decode()
    
    return f"{salt_hex}${hash_hex}"
def checkSenha(senhaDigitada: str, senhaHash: str) -> bool:
    salt_hex, hash_hex = senhaHash.split('$')
    salt = binascii.unhexlify(salt_hex)
    
    new_hash_bytes = hashlib.pbkdf2_hmac('sha256', senhaDigitada.encode(), salt, 100_000)
    new_hash_hex = binascii.hexlify(new_hash_bytes).decode()
    
    return hash_hex == new_hash_hex




# Create your views here.
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
            if checkSenha(password, Usuario.objects.get(nome=username).senha):
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