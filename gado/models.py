from django.db import models

class Animal(models.Model):
    numero_identificacao = models.CharField(max_length=20)
    raca = models.CharField(max_length=50)
    sexo = models.CharField(max_length=10)
    idade = models.IntegerField()
    cor = models.CharField(max_length=20)
    data_nascimento = models.DateField()
    data_aquisicao = models.DateField()
    data_venda_transferencia = models.DateField(null=True, blank=True)
    observacoes = models.TextField(blank=True)

    def __str__(self):
        return self.numero_identificacao
    
    
    class Meta:
        verbose_name_plural = "Animais"

class RegistroSanitario(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    data_vacinacao = models.DateField()
    tipo_vacina = models.CharField(max_length=50)
    tratamento_contra_parasitas = models.CharField(max_length=100)
    exames_veterinarios = models.CharField(max_length=100, blank=True)
    observacoes = models.TextField(blank=True)

    def __str__(self):
        return f"Sanitario - {self.animal.numero_identificacao}"

class RegistroAlimentacao(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    data_alimentacao = models.DateField()
    tipo_alimento = models.CharField(max_length=50)
    quantidade = models.FloatField()
    observacoes = models.TextField(blank=True)

    def __str__(self):
        return f"Alimentacao - {self.animal.numero_identificacao}"

class RegistroReprodutivo(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    data_cobertura = models.DateField()
    resultado_cobertura = models.CharField(max_length=20)
    observacoes = models.TextField(blank=True)

    def __str__(self):
        return f"Reprodutivo - {self.animal.numero_identificacao}"

# Adicione outros modelos conforme necessário, como RegistroProducaoLeite, RegistroPesagem, etc.