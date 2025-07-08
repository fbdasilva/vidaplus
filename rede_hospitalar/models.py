from django.db import models

class Unidade_Hospitalar(models.Model):
    unidade = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.unidade
