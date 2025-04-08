from django.shortcuts import render, redirect
from app_home.models import Cargos, Usuario, Item, Estoque, Emprestimo, Token
# from django.http import HttpResponseRedirect


# Create your views here.
def home(request):
    token = ""
    # print(Token.validar(request.session.get('token'))) TODO
    # token_id = Token.objects.get(usuario_id=Usuario.objects.get(id=request.session.get('id_user')).id).id
    
    # if not Token.isExpired(token_id):
        # print("DEBUG -> Token invalido!")
        # return redirect('/login')
    return render(request, 'app_home/global/index.html', context={'user': request.session.get('id_user') or None
                                                       , 'cargo': request.session.get('id_cargo') or None
                                                       , 'token': token})


def login(request):
    if request.method == 'GET':
        # if 'authorized' in request.session and request.session['authorized'] == True: TODO
            # return redirect('/')
        return render(request, 'app_home/pages/login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if Usuario.objects.filter(nome=username).exists():
            user_id = Usuario.objects.get(nome=username).id
            if Usuario.checkSenha(password, Usuario.objects.get(id=user_id).senha):
                user_cargo = Usuario.objects.get(id=user_id).cargo.id
                
                try: # user possui token no banco
                    # se o token estiver ok, retorna o token existente
                    if Token.isExpired(Token.objects.get(usuario_id=Usuario.objects.get(nome=username).id).id):
                        request.session['id_user'] = user_id
                        request.session['id_cargo'] = user_cargo
                        request.session['token'] = Token.objects.get(usuario_id=Usuario.objects.get(nome=username).id).token
                        return redirect('/')
                    
                    # se o token estiver expirado, deleta o token e gera um novo
                    else:
                        Token.objects.get(usuario_id=Usuario.objects.get(nome=username).id).delete()                        
                except Token.DoesNotExist:
                    pass # usuário nunca teve token no banco
                
                # gera um novo token para o usuário
                token_obj = Token.gerar_token(Usuario.objects.get(nome=username).id)
                request.session['id_user'] = user_id
                request.session['id_cargo'] = user_cargo
                request.session['token'] = token_obj.token
            
                return redirect('/')
            else:
                print("Senha incorreta") # senha incorreta TODO
                return redirect('/login')
        else:
            print("Usuário não encontrado") # usuário não encontrado TODO
            return redirect('/login')