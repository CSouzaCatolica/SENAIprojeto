import os, hashlib, binascii, uuid
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
from datetime import timedelta



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
    
    # senha com salt + hash
    def codSenha(senha: str) -> str:
        salt = os.urandom(32)
        hash_bytes = hashlib.pbkdf2_hmac('sha256', senha.encode(), salt, 100_000)
        salt_hex = binascii.hexlify(salt).decode()
        hash_hex = binascii.hexlify(hash_bytes).decode()
        return f"{salt_hex}${hash_hex}"
    
    def checkSenha(senhaDigitada: str, senhaHash: str) -> bool:
        salt_hex, hash_hex = senhaHash.split('$')
        salt = binascii.unhexlify(salt_hex)
        new_hash_bytes = hashlib.pbkdf2_hmac('sha256', senhaDigitada.encode(), salt, 100_000)
        new_hash_hex = binascii.hexlify(new_hash_bytes).decode()
        return hash_hex == new_hash_hex

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


class Token(models.Model):
    usuario = models.OneToOneField('Usuario', on_delete = models.CASCADE)
    token = models.CharField(max_length = 64, unique = True)
    criado_em = models.DateTimeField(auto_now_add = True)
    expira_em = models.DateTimeField()
    
    def __str__(self):
        return self.token

    def isExpired(TokenID):
        # retorna True se o token não estiver expirado
        try:
            Obj = Token.objects.get(id=TokenID)
        except Token.DoesNotExist:
            return True
        print(Obj.expira_em)
        print(timezone.now())
        print(Obj.expira_em > timezone.now())
        if timezone.now() > Obj.expira_em:
            return False
        return True
        
        
    @staticmethod
    def gerar_token(usuario_id):
        token = uuid.uuid4().hex
        expira = timezone.now() + timedelta(days=1, hours=12)
        obj, _ = Token.objects.update_or_create(
            usuario_id=usuario_id,
            defaults={'token': token, 'expira_em': expira}
        )
        return obj
