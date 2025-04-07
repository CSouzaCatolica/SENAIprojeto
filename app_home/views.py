from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.mail import send_mail

from app_home.models import PizzaModel


def home(request):
<<<<<<< HEAD
    print(request.session.get('pizza', []), request.session.get('quantidade_pizzas', 0))
    lista_produtos = PizzaModel.objects.all()
    return render(request, 'app_home/pages/home.html', context={'produtos': lista_produtos})


@login_required
def criar_pizza(request):
    if request.method == 'GET':
        return render(request, 'app_home/pages/pizza.html')
    
    pizza = request.POST.get('pizza')
    preco = request.POST.get('preco')
    imagem = request.POST.get('imagem')
    ingredientes = request.POST.get('ingredientes')
    pizza = PizzaModel.objects.create(pizza=pizza, preco=preco, imagem=imagem, ingredientes=ingredientes)
    return render(request, 'app_home/pages/pizza.html', context={'pizza': pizza})


@login_required
def listar_pizzas(request):
    pizzas = PizzaModel.objects.all()
    return render(request, 'app_home/pages/listar.html', context={'pizzas': pizzas})


@login_required
def deletar_pizza(request, id):
    pizza = PizzaModel.objects.get(id=id)
    pizza.delete()
    return redirect('listar') 


@login_required
def atualizar_pizza(request, id):
    if request.method == 'GET':
        pizza = PizzaModel.objects.get(id=id)
        return render(request, 'app_home/pages/atualizar_pizza.html', context={'pizza': pizza})
    
    pizza = request.POST.get('pizza')
    preco = request.POST.get('preco')
    imagem = request.POST.get('imagem')
    ingredientes = request.POST.get('ingredientes')
    PizzaModel.objects.filter(id=id).update(pizza=pizza, preco=preco, imagem=imagem, ingredientes=ingredientes)
    return redirect('listar')


def carrinho_pizza(request, id):
    pizzas = request.session.get('pizza', [])
    pizzas.append(id)
    request.session['pizza'] = pizzas

    quantidade_pizzas = len(pizzas)
    request.session['quantidade_pizzas'] = quantidade_pizzas
    return redirect('home')


def comprar_carrinho_pizza(request):
    pizzas = request.session.get('pizza', [])
    lista_pizzas = [PizzaModel.objects.get(id=pizza) for pizza in pizzas]
    
    return render(request, 'app_home/pages/listar_carrinho.html', {
        'pizzas': lista_pizzas,
        'quantidade_pizzas': len(pizzas)
    })


def mandar_email(usuario, mensagem, titulo):
    print(f'Enviando email para {usuario} com a mensagem: {mensagem}')
    send_mail(
        titulo,
        mensagem,
        'seu_email@gmail.com',
        [usuario],
        fail_silently=False,
    )


# === LOGIN VIEW ===
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
            return redirect('login')
    return render(request, 'app_home/pages/login.html')


# === LOGOUT VIEW ===
def logout_view(request):
    logout(request)
    return redirect('home')
=======
    pizzas = [
        {'nome': 'Calabresa', 'descricao': 'Pizza de calabresa', 'preco': 20.99, 'img': 'https://media.discordapp.net/attachments/1035029551375454248/1356075306074509382/pizza.png?ex=67eb3f0b&is=67e9ed8b&hm=9c30f1d0a9374f322c374d246b3aa1b8fd49baa107bdc6b61f1ed6c2daa5d49c&=&format=webp&quality=lossless'},
        {'nome': 'Mussarela', 'descricao': 'Pizza de mussarela', 'preco': 19.99, 'img': 'https://media.discordapp.net/attachments/1035029551375454248/1356075306074509382/pizza.png?ex=67eb3f0b&is=67e9ed8b&hm=9c30f1d0a9374f322c374d246b3aa1b8fd49baa107bdc6b61f1ed6c2daa5d49c&=&format=webp&quality=lossless'},
        {'nome': 'Portuguesa', 'descricao': 'Pizza de portuguesa', 'preco': 22.99, 'img': 'https://media.discordapp.net/attachments/1035029551375454248/1356075306074509382/pizza.png?ex=67eb3f0b&is=67e9ed8b&hm=9c30f1d0a9374f322c374d246b3aa1b8fd49baa107bdc6b61f1ed6c2daa5d49c&=&format=webp&quality=lossless'},
    ]

    return render(request, 'app_home/pages/home.html', {'pizzas': pizzas})
>>>>>>> main
