from django.db import models

# Create your models here.

class Produtos(models.Model):
    
    nome = models.CharField(max_length=255, null=False)
    marca = models.CharField(max_length=255, null=False)
    valor = models.FloatField()
    estoque = models.IntegerField()


    def __str__(self):
        return "{} - {}".format(self.nome, self.marca, self.valor, self.estoque)