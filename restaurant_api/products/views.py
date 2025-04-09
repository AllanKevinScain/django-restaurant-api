from django.http import HttpResponse


def index(request):
    return HttpResponse("Olá, Você está na index do app produtos.")
