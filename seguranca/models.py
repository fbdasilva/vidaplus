from django.db import models
from django.contrib.auth.models import User

class PerfilUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cargo = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.user.username} - {self.cargo}"

class RegistroAuditoria(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    acao = models.CharField(max_length=100)
    modelo_afetado = models.CharField(max_length=100)
    objeto_id = models.PositiveIntegerField(null=True, blank=True)
    data_hora = models.DateTimeField(auto_now_add=True)
    detalhes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.usuario} - {self.acao} - {self.modelo_afetado}"
