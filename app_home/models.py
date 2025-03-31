from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class PizzaModel(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(
        max_digits=5, 
        decimal_places=2,
        validators=[
            MinValueValidator(0.01),
            MaxValueValidator(999.99)
        ])
    imagem = models.URLField()
    descricao = models.TextField()
    
    criado_em = models.DateTimeField(auto_now_add=True)
    alterado_em = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return f"Pizza: {self.name} ({self.preco})"
    