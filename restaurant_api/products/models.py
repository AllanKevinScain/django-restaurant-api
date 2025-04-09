from django.db import models


class Categorias(models.Model):
    nome = models.CharField(max_length=200)  # Exemplo: Pizza, Café, Burguer

    def __str__(self):
        return self.nome


class Produtos(models.Model):
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    # Exemplo: Pizza de Camarão, Café Cremoso, Burguer Triplo Capeado com Queijo
    nome = models.CharField(max_length=200)
    preco = models.FloatField(default=0)
    descricao = models.CharField(max_length=200)

    def __str__(self):
        return self.nome
