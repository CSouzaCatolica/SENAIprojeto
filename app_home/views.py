from decimal import Decimal
from django.shortcuts import render, redirect
from app_home.models import PizzaModel
# extenção legal é a codeium


# Create your views here.
def home(request):
    # pizzas = [
    #     {'nome': 'Calabresa', 'descricao': 'Pizza de calabresa', 'preco': 20.99, 'img': 'https://media.discordapp.net/attachments/1035029551375454248/1356075306074509382/pizza.png?ex=67eb3f0b&is=67e9ed8b&hm=9c30f1d0a9374f322c374d246b3aa1b8fd49baa107bdc6b61f1ed6c2daa5d49c&=&format=webp&quality=lossless'},
    #     {'nome': 'Mussarela', 'descricao': 'Pizza de mussarela', 'preco': 19.99, 'img': 'https://media.discordapp.net/attachments/1035029551375454248/1356075306074509382/pizza.png?ex=67eb3f0b&is=67e9ed8b&hm=9c30f1d0a9374f322c374d246b3aa1b8fd49baa107bdc6b61f1ed6c2daa5d49c&=&format=webp&quality=lossless'},
    #     {'nome': 'Portuguesa', 'descricao': 'Pizza de portuguesa', 'preco': 22.99, 'img': 'https://media.discordapp.net/attachments/1035029551375454248/1356075306074509382/pizza.png?ex=67eb3f0b&is=67e9ed8b&hm=9c30f1d0a9374f322c374d246b3aa1b8fd49baa107bdc6b61f1ed6c2daa5d49c&=&format=webp&quality=lossless'},
    # ]
    pizzas = PizzaModel.objects.all()
    # O método all() retorna todos os objetos do modelo PizzaModel. Isso é útil para exibir uma lista de pizzas na página inicial.
    return render(request, 'app_home/pages/home.html', {'pizzas': pizzas})


def criar_pizza(request):
    if request.method == 'GET':
        # Renderizar o formulário para criar uma nova pizza
        return render(request, 'app_home/pages/criar_pizza.html')
    elif request.method == 'POST':
        
        # Os dados do formulário são enviados via POST conforme o .get('nome') é
        # equivalente ao nome dentro do form do html criar_pizza.html <input type="*" nome="nome"> ele se guia pelo att nome
        nome = request.POST.get('nome')
        preco = request.POST.get('preco')
        img = request.POST.get('img')
        descricao = request.POST.get('descricao')
        pizza = PizzaModel.objects.create(
            nome=nome, 
            preco=preco, 
            imagem=img, 
            descricao=descricao
        )
        # pizza = PizzaModel(nome=nome, preco=preco, img=img, descricao=descricao)
        # pizza.save()
        return render(request, 'app_home/pages/home.html', context={'pizzas': [pizza]})
    
    
def listar_pizzas(request):
    pizzas = PizzaModel.objects.all()
    return render(request, 'app_home/pages/listar.html', context={'pizzas': pizzas})

def deletar_pizza(request, id):
    pizza = PizzaModel.objects.get(id=id)
    pizza.delete()
    return redirect('listar_pizzas')

def editar_pizza(request, id):
    if request.method == 'GET':
        pizza = PizzaModel.objects.get(id=id)    
        return render(request, 'app_home/pages/editar_pizza.html', context={'pizza': pizza})
    # O método GET é usado para obter dados do servidor. Neste caso, ele está buscando uma pizza específica com base no ID fornecido na URL.
    elif request.method == 'POST':
        pizza = PizzaModel.objects.get(id=id)
        pizza.nome = request.POST.get('nome')
        pizza.preco = Decimal(request.POST.get('preco').replace(',', '.'))
        pizza.preco = request.POST.get('preco')

        pizza.imagem = request.POST.get('img')
        pizza.descricao = request.POST.get('descricao')
        PizzaModel.objects.filter(id=id).update(
            nome=pizza.nome, 
            preco=pizza.preco, 
            imagem=pizza.imagem, 
            descricao=pizza.descricao
        )
        return redirect('listar_pizzas')