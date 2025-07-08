from django.db import models

from profissionais.models import Medico, Tecnico, Enfermeiro
from rede_hospitalar.models import Unidade_Hospitalar

class Paciente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    data_nascimento = models.DateField()
    historico_clinico = models.TextField(blank=True)

    def __str__(self):
        return self.nome

class Consulta(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    data = models.DateTimeField()
    resumo = models.CharField(max_length=200, null=True)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE, null=True)
    unidade = models.ForeignKey(Unidade_Hospitalar, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.paciente} - {self.data}"

class Exame(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    resumo = models.CharField(max_length=200, null=True)
    data = models.DateField()
    unidade = models.ForeignKey(Unidade_Hospitalar, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.resumo} - {self.paciente}"

class Prontuario(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    data_abertura = models.DateField(auto_now_add=True)
    historico = models.TextField()
    consultas = models.ManyToManyField('Consulta', related_name='prontuarios', blank=True)
    exames = models.ManyToManyField('Exame', related_name='prontuarios', blank=True)

    def __str__(self):
        return f"Prontuário {self.paciente.nome} - {self.data_abertura}"
