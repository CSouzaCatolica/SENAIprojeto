from django.shortcuts import render
from app_home.models import PizzaModel

# Create your views here.
def home(request):
    return render(request, 'app_home/global/index.html')