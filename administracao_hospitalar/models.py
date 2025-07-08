
from django.db import models
from rede_hospitalar.models import Unidade_Hospitalar

class Leito(models.Model):
    unidade = models.ForeignKey(Unidade_Hospitalar, on_delete=models.CASCADE)
    numero = models.CharField(max_length=10)
    tipo = models.CharField(max_length=50, choices=[('enfermaria', 'Enfermaria'), ('uti', 'UTI')])
    ocupado = models.BooleanField(default=False)

    def __str__(self):
        return f"Leito {self.numero} - {self.unidade}"

class RelatorioFinanceiro(models.Model):
    unidade = models.ForeignKey(Unidade_Hospitalar, on_delete=models.CASCADE)
    receitas = models.DecimalField(max_digits=12, decimal_places=2)
    despesas = models.DecimalField(max_digits=12, decimal_places=2)

    @property
    def saldo(self):
        return self.receitas - self.despesas

class Suprimento(models.Model):
    unidade = models.ForeignKey(Unidade_Hospitalar, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    quantidade = models.IntegerField()

    def __str__(self):
        return f"{self.nome} ({self.quantidade}) - {self.unidade}"