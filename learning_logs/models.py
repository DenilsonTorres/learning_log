from django.db import models
from django.contrib.auth.models import User


# Criação de Topicos
class Topic(models.Model):
    """Um assunto que o usuário está aprendendo"""

    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Devolve uma string do model"""
        return self.text


class Entry(models.Model):
    """Algo específico aprendido sobre um assunto"""

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "entries"

    def __str__(self):
        """Devolve uma string do model"""
        return self.text[:50] + "..."
