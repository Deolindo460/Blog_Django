from django.db import models
from django.utils import timezone

# Create your models here.

class Postagem(models.Model):
    data_hora = models.DateTimeField(default=timezone.now)
    conteudo = models.TextField(blank=True)
    categoria = models.CharField(max_length=15)
    descricao = models.CharField(max_length=400)
    titulo = models.CharField(max_length=100)
    imagem = models.DO_NOTHING
    autor = models.CharField(max_length=30)


