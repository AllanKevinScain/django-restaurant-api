from django.contrib import admin

from .models import Categorias, Produtos


@admin.register(Categorias)
class CategoriasAdmin(admin.ModelAdmin):
    list_display = ("nome",)


@admin.register(Produtos)
class ProdutosAdmin(admin.ModelAdmin):
    list_display = ("categoria", "nome", "preco", "descricao")
    list_filter = ("categoria",)  # a , aponto que é uma tupla
