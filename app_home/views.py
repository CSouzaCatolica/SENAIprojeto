from django.shortcuts import render
from app_home.models import PizzaModel

# Create your views here.
def home(request):
    pizzas = [
        {'nome': 'Calabresa', 'descricao': 'Pizza de calabresa', 'preco': 20.99, 'img': 'https://media.discordapp.net/attachments/1035029551375454248/1356075306074509382/pizza.png?ex=67eb3f0b&is=67e9ed8b&hm=9c30f1d0a9374f322c374d246b3aa1b8fd49baa107bdc6b61f1ed6c2daa5d49c&=&format=webp&quality=lossless'},
        {'nome': 'Mussarela', 'descricao': 'Pizza de mussarela', 'preco': 19.99, 'img': 'https://media.discordapp.net/attachments/1035029551375454248/1356075306074509382/pizza.png?ex=67eb3f0b&is=67e9ed8b&hm=9c30f1d0a9374f322c374d246b3aa1b8fd49baa107bdc6b61f1ed6c2daa5d49c&=&format=webp&quality=lossless'},
        {'nome': 'Portuguesa', 'descricao': 'Pizza de portuguesa', 'preco': 22.99, 'img': 'https://media.discordapp.net/attachments/1035029551375454248/1356075306074509382/pizza.png?ex=67eb3f0b&is=67e9ed8b&hm=9c30f1d0a9374f322c374d246b3aa1b8fd49baa107bdc6b61f1ed6c2daa5d49c&=&format=webp&quality=lossless'},
    ]

    return render(request, 'app_home/pages/home.html', {'pizzas': pizzas})