from django.contrib import admin

from .models import Categorias, Produtos

admin.site.register(Categorias)


@admin.register(Produtos)
class AlternativaAdmin(admin.ModelAdmin):
    list_display = ("categoria", "nome", "preco", "descricao")
    list_filter = ("categoria",)  # a , aponto que é uma tupla
