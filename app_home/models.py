from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Cargos(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome


class Usuario(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=255)
    cargo = models.ForeignKey(Cargos, on_delete=models.SET_NULL, null=True, related_name='usuarios')
    d_admissao = models.DateField()
    d_demissao = models.DateField(null=True, blank=True)
    status = models.BooleanField(default=1)

    def __str__(self):
        return self.nome


class Item(models.Model):
    nome = models.CharField(max_length=255)
    img_ref = models.CharField(max_length=255, null=True, blank=True)
    quantidade = models.IntegerField()
    d_vencimento = models.DateField(null=True, blank=True)
    status = models.BooleanField(default=1)

    def __str__(self):
        return self.nome


class Estoque(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='estoques')
    quantidade = models.BigIntegerField()
    deleted = models.BooleanField(default=0)


class Emprestimo(models.Model):
    solicitante = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='emprestimos_feitos')
    destinatario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='emprestimos_recebidos')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='emprestimos')
    d_emprestimo = models.DateField()
    d_devolucao = models.DateField()
    d_devolvido = models.DateField(null=True, blank=True)
    quantidade = models.IntegerField()
    status = models.BooleanField(default=1)
