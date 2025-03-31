from django.shortcuts import render
from app_home.models import PizzaModel

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
        # equivalente ao nome dentro do form do html criar_pizza.html <input type="*" name="nome"> ele se guia pelo att name
        nome = request.POST.get('nome')
        preco = request.POST.get('preco')
        img = request.POST.get('img')
        descricao = request.POST.get('descricao')
        pizza = PizzaModel.objects.create(
            name=nome, 
            preco=preco, 
            imagem=img, 
            ingredientes=descricao
        )
        # pizza = PizzaModel(nome=nome, preco=preco, img=img, descricao=descricao)
        # pizza.save()
        return render(request, 'app_home/pages/home.html', context={'pizzas': [pizza]})