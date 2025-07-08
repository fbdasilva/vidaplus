from django.db import models
from pacientes.models import Paciente
from profissionais.models import Medico

class AtendimentoOnline(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)
    tipo = models.CharField(max_length=50, choices=[('video', 'Vídeo'), ('chat', 'Chat')])

    def __str__(self):
        return f"{self.paciente} - {self.medico} - {self.data.strftime('%d/%m/%Y %H:%M')}"

class PrescricaoOnline(models.Model):
    data = models.DateField(auto_now_add=True)
    medicamento = models.CharField(max_length=100)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE, null=True)
    observacoes = models.TextField(blank=True,null=True)

    def __str__(self):
        return f"{self.medicamento}"

class VideoChamada(models.Model):
    data = models.DateField(auto_now_add=True)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE, null=True)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.paciente} - {self.medico}"