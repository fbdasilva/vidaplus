from django.contrib import admin

# Register your models here.
from .models import Paciente, Exame, Consulta, Prontuario

admin.site.register(Paciente)
admin.site.register(Exame)
admin.site.register(Consulta)
admin.site.register(Prontuario)