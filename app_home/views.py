from datetime import datetime
from django.shortcuts import render, redirect
from app_home.models import Cargos, Usuario, Item, Estoque, Emprestimo

def get_context(request) -> dict:
    context = {}
    context["usuario"] = request.session.get('usuario') or None
    context["cargo"] = request.session.get('id_cargo') or None
    context["token"] = request.session.get('token') or False
    return context


# Create your views here.
def dev(request):
    return render(request, 'app_home/pages/cadastro.html')

#---==================================================================================================---
#                   views
#---==================================================================================================---

def home(request):

    return render(request, 'app_home/global/index.html', context = get_context(request))

def view_cargos(request):
    ctx = get_context(request)
    ctx['cargos'] = Cargos.objects.all()
    return render(request, 'app_home/pages/cargos.html', context = get_context(request))

def view_itens(request):
    ctx = get_context(request)
    ctx['itens'] = Item.objects.all()
    return render(request, 'app_home/pages/itens.html', context = get_context(request))

def view_emprestimos(request):
    ctx = get_context(request)
    ctx['emprestimos'] = Emprestimo.objects.all()
    return render(request, 'app_home/pages/emprestimos.html', context = get_context(request))

def view_estoque(request):
    ctx = get_context(request)
    ctx['estoque'] = Estoque.objects.all()
    return render(request, 'app_home/pages/estoque.html', context = get_context(request))

def view_usuarios(request):
    ctx = get_context(request)
    ctx['usuarios'] = Usuario.objects.all()
    return render(request, 'app_home/pages/usuarios.html', context = get_context(request))



def logout(request):
    if request.method == 'GET':
        request.session.flush()
        return redirect('/')
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

  
  
  
#---==================================================================================================---
#                   Users
#---==================================================================================================---

  
        
def get_user(request, id):
    
    if request.method == 'GET':
        if id:
            if Usuario.objects.filter(id=id).exists():
                ctx = get_context(request)
                ctx['get_user'] = {
                    'id': id,
                    'nome': Usuario.objects.get(id=id).nome,
                    'cargo': Cargos.objects.get(id=Usuario.objects.get(id=id).cargo.id).nome,
                    'email': Usuario.objects.get(id=id).email,
                    'd_admissao': Usuario.objects.get(id=id).d_admissao,
                    'd_demissao': Usuario.objects.get(id=id).d_demissao
                }
                print(ctx)
        
                return render(request, 'app_home/components/header.html', context = ctx)
            else:
                print("Usuário nao encontrado")
        else:
            print("Falta de parametro id")
    return render(request, 'app_home/components/header.html', context = get_context(request))
        
def get_allUsers(request):
    if request.method == 'GET':
        usuarios = Usuario.objects.all()
        return render(request, 'app_home/components/header.html', context = {'usuarios': usuarios})

def delete_user(request, id):
    ctx = get_context(request)
    if request.method == 'POST':
        if id:
            if Usuario.objects.filter(id=id).exists():
                Usuario.objects.filter(id=id).delete()
                return redirect('/get_allUsers', context = get_context(request), status=200)
            else:
                ctx['error'] = "Usuário nao encontrado" # print("Usuário nao encontrado")
        else:
            ctx['error'] = "Falta de parametro id" # print("Falta de parametro id")
        return redirect('/get_allUsers', context = ctx, status=400)

def update_user(request, id):
    ctx = get_context(request)
    if request.method == 'POST':
        if id:
            if Usuario.objects.filter(id=id).exists():
                Usuario.objects.filter(id=id).update(
                    nome = request.POST.get('nome'),
                    email = request.POST.get('email'),
                    senha = request.POST.get('senha'),
                    cargo = Cargos.objects.get(id=request.POST.get('cargo')),
                    d_admissao = request.POST.get('d_admissao')
                    # TODO criar botão de demitir d_demissao = request.POST.get('d_demissao'),
                    # TODO criar botão de demitir status = request.POST.get('status')
                )
                return redirect('/get_allUsers', context = get_context(request), status=200)
            else:
                ctx['error'] = "Usuário nao encontrado" # print("Usuário nao encontrado")
        else:    
            ctx['error'] = "Falta de parametro id" # print("Falta de parametro id")
        return redirect('/get_allUsers', context = ctx, status=400)
        

def create_user(request):
    ctx = get_context(request)
    
    if request.method == 'POST':
        if request.POST.get('nome') and request.POST.get('email') and request.POST.get('senha') and request.POST.get('cargo') and request.POST.get('pfp_ref'):
            newUser = Usuario.objects.create(
                nome = request.POST.get('nome'),
                email = request.POST.get('email'),
                senha = Usuario.codSenha(request.POST.get('senha')),
                pfp_ref = request.POST.get('pfp_ref'),
                cargo = Cargos.objects.get(id=request.POST.get('cargo')),
                d_admissao = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            )
            ctx['newUser'] = newUser
            return redirect('/get_allUsers', context = ctx, status=200)
        else:
            ctx['error'] = "Falta de parametro" # print("Falta de parametro")
        return redirect('/get_allUsers', context = ctx, status=400)
    
    
    
    
    
    
    
#---==================================================================================================---
#                   Itens
#---==================================================================================================---


def create_item(request):
    ctx = get_context(request)
    if request.method == 'POST':
        if request.POST.get('nome') and request.POST.get('img_ref') and request.POST.get('quantidade') and request.POST.get('d_vencimento'):
            newItem = Item.objects.create(
                nome = request.POST.get('nome'),
                img_ref = request.POST.get('img_ref'),
                quantidade = request.POST.get('quantidade'),
                d_vencimento = request.POST.get('d_vencimento'),
            )
            ctx['newItem'] = newItem
            return redirect('/get_allItems', context = ctx, status=200)
        else:
            ctx['error'] = "Falta de parametro" # print("Falta de parametro")
        return redirect('/get_allItems', context = ctx, status=400)
    
def get_allItems(request):
    if request.method == 'GET':
        items = Item.objects.all()
        return render(request, 'app_home/components/header.html', context = {'items': items})  

def delete_item(request, id):
    ctx = get_context(request)
    if request.method == 'POST':
        if id:
            if Item.objects.filter(id=id).exists():
                Item.objects.filter(id=id).delete()
                return redirect('/get_allItems', context = get_context(request), status=200)
            else:
                ctx['error'] = "Item nao encontrado" # print("Item nao encontrado")
        else:
            ctx['error'] = "Falta de parametro id" # print("Falta de parametro id")
        return redirect('/get_allItems', context = ctx, status=400)

def update_item(request, id):
    ctx = get_context(request)
    if request.method == 'POST':
        if id:
            if Item.objects.filter(id=id).exists():
                Item.objects.filter(id=id).update(
                    nome = request.POST.get('nome'),
                    img_ref = request.POST.get('img_ref'),
                    quantidade = request.POST.get('quantidade'),
                    d_vencimento = request.POST.get('d_vencimento')
                )
                return redirect('/get_allItems', context = get_context(request), status=200)
            else:
                ctx['error'] = "Item nao encontrado" # print("Item nao encontrado")
        else:    
            ctx['error'] = "Falta de parametro id" # print("Falta de parametro id")
        return redirect('/get_allItems', context = ctx, status=400)
    
def get_item(request, id):
    
    if request.method == 'GET':
        if id:
            if Item.objects.filter(id=id).exists():
                ctx = get_context(request)
                ctx['get_item'] = {
                    'id': id,
                    'nome': Item.objects.get(id=id).nome,
                    'img_ref': Item.objects.get(id=id).img_ref,
                    'quantidade': Item.objects.get(id=id).quantidade,
                    'd_vencimento': Item.objects.get(id=id).d_vencimento
                }
                print(ctx)
        
                return render(request, 'app_home/components/header.html', context = ctx)
            else:
                print("Item nao encontrado")
        else:
            print("Falta de parametro id")
    return render(request, 'app_home/components/header.html', context = get_context(request))

def get_allItemsByUser(request, id):
    if request.method == 'GET':
        if id:
            if Usuario.objects.filter(id=id).exists():
                items = Item.objects.filter(usuario=id)
                return render(request, 'app_home/components/header.html', context = {'items': items})
            else:
                print("Usuario nao encontrado")
        else:
            print("Falta de parametro id")
    return render(request, 'app_home/components/header.html', context = get_context(request))


#---==================================================================================================---
#                   cargos
#---==================================================================================================---

def get_allCargos(request):
    if request.method == 'GET':
        cargos = Cargos.objects.all()
        return render(request, 'app_home/components/header.html', context = {'cargos': cargos})
    
def create_cargo(request):
    ctx = get_context(request)
    if request.method == 'POST':
        if request.POST.get('nome'):
            newCargo = Cargos.objects.create(
                nome = request.POST.get('nome')
            )
            ctx['newCargo'] = newCargo
            return redirect('/get_allCargos', context = ctx, status=200)
        else:
            ctx['error'] = "Falta de parametro" # print("Falta de parametro")
        return redirect('/get_allCargos', context = ctx, status=400)
    
def delete_cargo(request, id):
    ctx = get_context(request)
    if request.method == 'POST':
        if id:
            if Cargos.objects.filter(id=id).exists():
                Cargos.objects.filter(id=id).delete()
                return redirect('/get_allCargos', context = get_context(request), status=200)
            else:
                ctx['error'] = "Cargo nao encontrado" # print("Cargo nao encontrado")
        else:
            ctx['error'] = "Falta de parametro id" # print("Falta de parametro id")
        return redirect('/get_allCargos', context = ctx, status=400)
    
def update_cargo(request, id):
    ctx = get_context(request)
    if request.method == 'POST':
        if id:
            if Cargos.objects.filter(id=id).exists():
                Cargos.objects.filter(id=id).update(
                    nome = request.POST.get('nome')
                )
                return redirect('/get_allCargos', context = get_context(request), status=200)
            else:
                ctx['error'] = "Cargo nao encontrado" # print("Cargo nao encontrado")
        else:    
            ctx['error'] = "Falta de parametro id" # print("Falta de parametro id")
        return redirect('/get_allCargos', context = ctx, status=400)
    
def get_cargo(request, id):
    
    if request.method == 'GET':
        if id:
            if Cargos.objects.filter(id=id).exists():
                ctx = get_context(request)
                ctx['get_cargo'] = {
                    'id': id,
                    'nome': Cargos.objects.get(id=id).nome
                }
                print(ctx)
        
                return render(request, 'app_home/components/header.html', context = ctx)
            else:
                print("Cargo nao encontrado")
        else:
            print("Falta de parametro id")
    return render(request, 'app_home/components/header.html', context = get_context(request))






#---==================================================================================================---
#                   estoque
#---==================================================================================================---



def get_allEstoque(request):
    if request.method == 'GET':
        estoque = Estoque.objects.all()
        return render(request, 'app_home/components/header.html', context = {'estoque': estoque})
    
def create_estoque(request):
    ctx = get_context(request)
    if request.method == 'POST':
        if request.POST.get('item') and request.POST.get('quantidade'):
            newEstoque = Estoque.objects.create(
                item = Item.objects.get(id=request.POST.get('item')), # TODO criar botão de adicionar item
                quantidade = request.POST.get('quantidade')
            )
            ctx['newEstoque'] = newEstoque
            return redirect('/get_allEstoque', context = ctx, status=200)
        else:
            ctx['error'] = "Falta de parametro" # print("Falta de parametro")
        return redirect('/get_allEstoque', context = ctx, status=400)
    
def delete_estoque(request, id):
    ctx = get_context(request)
    if request.method == 'POST':
        if id:
            if Estoque.objects.filter(id=id).exists():
                Estoque.objects.filter(id=id).delete()
                return redirect('/get_allEstoque', context = get_context(request), status=200)
            else:
                ctx['error'] = "Estoque nao encontrado" # print("Estoque nao encontrado")
        else:
            ctx['error'] = "Falta de parametro id" # print("Falta de parametro id")
        return redirect('/get_allEstoque', context = ctx, status=400)
    
def update_estoque(request, id):
    ctx = get_context(request)
    if request.method == 'POST':
        if id:
            if Estoque.objects.filter(id=id).exists():
                Estoque.objects.filter(id=id).update(
                    item = Item.objects.get(id=request.POST.get('item')), # TODO criar botão de adicionar item
                    quantidade = request.POST.get('quantidade')
                )
                return redirect('/get_allEstoque', context = get_context(request), status=200)
            else:
                ctx['error'] = "Estoque nao encontrado" # print("Estoque nao encontrado")
        else:    
            ctx['error'] = "Falta de parametro id" # print("Falta de parametro id")
        return redirect('/get_allEstoque', context = ctx, status=400)
    
def get_estoque(request, id):
    
    if request.method == 'GET':
        if id:
            if Estoque.objects.filter(id=id).exists():
                ctx = get_context(request)
                ctx['get_estoque'] = {
                    'id': id,
                    'item': Estoque.objects.get(id=id).item, # TODO criar botão de adicionar item
                    'quantidade': Estoque.objects.get(id=id).quantidade
                }
                print(ctx)
        
                return render(request, 'app_home/components/header.html', context = ctx)
            else:
                print("Estoque nao encontrado")
        else:
            print("Falta de parametro id")
    return render(request, 'app_home/components/header.html', context = get_context(request))





#---==================================================================================================---
#                   Emprestimo
#---==================================================================================================---


def get_allEmprestimos(request):
    if request.method == 'GET':
        emprestimos = Emprestimo.objects.all()
        return render(request, 'app_home/components/header.html', context = {'emprestimos': emprestimos})   
    
def create_emprestimo(request):
    ctx = get_context(request)
    if request.method == 'POST':
        if request.POST.get('usuario') and request.POST.get('item') and request.POST.get('quantidade'):
            newEmprestimo = Emprestimo.objects.create(
                usuario = Usuario.objects.get(id=request.POST.get('usuario')), # TODO criar botão de adicionar usuario
                item = Item.objects.get(id=request.POST.get('item')), # TODO criar botão de adicionar item
                quantidade = request.POST.get('quantidade')
            )
            ctx['newEmprestimo'] = newEmprestimo
            return redirect('/get_allEmprestimos', context = ctx, status=200)
        else:
            ctx['error'] = "Falta de parametro" # print("Falta de parametro")
        return redirect('/get_allEmprestimos', context = ctx, status=400)
    
def delete_emprestimo(request, id):
    ctx = get_context(request)
    if request.method == 'POST':
        if id:
            if Emprestimo.objects.filter(id=id).exists():
                Emprestimo.objects.filter(id=id).delete()
                return redirect('/get_allEmprestimos', context = get_context(request), status=200)
            else:
                ctx['error'] = "Emprestimo nao encontrado" # print("Emprestimo nao encontrado")
        else:
            ctx['error'] = "Falta de parametro id" # print("Falta de parametro id")
        return redirect('/get_allEmprestimos', context = ctx, status=400)    

def update_emprestimo(request, id):    
    ctx = get_context(request)
    if request.method == 'POST':
        if id:
            if Emprestimo.objects.filter(id=id).exists():
                Emprestimo.objects.filter(id=id).update(
                    usuario = Usuario.objects.get(id=request.POST.get('usuario')), # TODO criar botão de adicionar usuario
                    item = Item.objects.get(id=request.POST.get('item')), # TODO criar botão de adicionar item
                    quantidade = request.POST.get('quantidade')
                )
                return redirect('/get_allEmprestimos', context = get_context(request), status=200)
            else:
                ctx['error'] = "Emprestimo nao encontrado" # print("Emprestimo nao encontrado")
        else:    
            ctx['error'] = "Falta de parametro id" # print("Falta de parametro id")
        return redirect('/get_allEmprestimos', context = ctx, status=400)
    
    
def get_emprestimo(request, id):
    
    if request.method == 'GET':
        if id:
            if Emprestimo.objects.filter(id=id).exists():
                ctx = get_context(request)
                ctx['get_emprestimo'] = {
                    'id': id,
                    'usuario': Emprestimo.objects.get(id=id).usuario, # TODO criar botão de adicionar usuario
                    'item': Emprestimo.objects.get(id=id).item, # TODO criar botão de adicionar item
                    'quantidade': Emprestimo.objects.get(id=id).quantidade
                }
                print(ctx)
        
                return render(request, 'app_home/components/header.html', context = ctx)
            else:
                print("Emprestimo nao encontrado")
        else:
            print("Falta de parametro id")
    return render(request, 'app_home/components/header.html', context = get_context(request))

def get_allEmprestimosByUser(request, id):
    if request.method == 'GET':
        if id:
            emprestimos = Emprestimo.objects.filter(usuario=id)
            return render(request, 'app_home/components/header.html', context = {'emprestimos': emprestimos})
    
def get_allEmprestimosByItem(request, id):
    if request.method == 'GET':
        if id:
            emprestimos = Emprestimo.objects.filter(item=id)
            return render(request, 'app_home/components/header.html', context = {'emprestimos': emprestimos})
    