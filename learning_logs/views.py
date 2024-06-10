from django.shortcuts import render


def index(request):
    # Página inicial
    return render(request, "learning_logs/index.html")
