from django.db import models

class ProfissionalSaude(models.Model):
    nome = models.CharField(max_length=100)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.nome

class Medico(ProfissionalSaude):
    especialidade = models.CharField(max_length=100, blank=True)
    crm = models.CharField(max_length=15, unique=True)

class Enfermeiro(ProfissionalSaude):
    coren = models.CharField(max_length=15, unique=True)

class Tecnico(ProfissionalSaude):
    area_atuacao = models.CharField(max_length=100)

class Prescricao(models.Model):
    medicamento = models.CharField(max_length=100, null=True)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE, null=True)
    data = models.DateField(auto_now_add=True,null=True)
    observacoes = models.TextField(blank=True,null=True)

    def __str__(self):
        return f"{self.medicamento}"