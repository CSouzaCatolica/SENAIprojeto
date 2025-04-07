from django.contrib import admin
from .models import Cargos, Usuario, Item, Estoque, Emprestimo

# Register your models here.

admin.site.register(Cargos)
admin.site.register(Usuario)
admin.site.register(Item)
admin.site.register(Estoque)
admin.site.register(Emprestimo)