from django.shortcuts import render

# Create your views here.
def home(request):
    teste_arr = [
        {
            'nome': 'Python',
            'descricao': 'Linguagem de programação de alto nível'
        },
        {
            'nome': 'Django',
            'descricao': 'Framework para desenvolvimento web'
        }
    ]

    return render(request, 'app_home/pages/index.html', context={'teste': teste_arr})