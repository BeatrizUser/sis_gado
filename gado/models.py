from django.db import models

class Animal(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    peso = models.FloatField()
    data_nascimento = models.DateField()
    # Outros campos relevantes

    def __str__(self):
        return self.nome
