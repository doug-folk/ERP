from django.db import models

# Create your models here.
class Funcionario(models.Model):
    nome = models.CharField(
        max_length=40,
        null = False,
        blank = False
    )
    sobrenome = models.CharField(
        max_length=70,
        null = False,
        blank = False
    )
    cpf = models.CharField(
        max_length=14,
        null = False,
        blank = False
        )
    email = models.EmailField(
        max_length=50,
        null = False,
        blank = False
        )
    remuneracao = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        null = False,
        blank = False
    )


    def __str__(self):
        return f"ID {self.id} - {self.nome} {self.sobrenome}"
        
class Produto(models.Model):
    nome = models.CharField(
        max_length=50,
        null = False,
        blank = False
    )
    descricao = models.CharField(
        max_length=255,
        null = False,
        blank = False
    )
    preco = models.DecimalField(
        max_digits = 7,
        decimal_places =2 ,
        null = False,
        blank = False
    )

    imagem = models.ImageField(
        null=True,
        blank=True,
        upload_to='imagens-produtos'
    )


    def __str__(self):
        return f"ID {self.id} - {self.nome} Preço: {self.preco}"

class Venda(models.Model):
    funcionario = models.ForeignKey(
        'Funcionario',
        on_delete = models.CASCADE,
    )
    produto = models.ForeignKey(
        'Produto',
        on_delete = models.CASCADE
    )

    data_hora = models.DateTimeField(
        auto_now_add=True,

    )