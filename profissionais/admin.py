from django.contrib import admin

# Register your models here.
from .models import Medico, Tecnico, Enfermeiro, Prescricao

admin.site.register(Medico)
admin.site.register(Tecnico)
admin.site.register(Enfermeiro)
admin.site.register(Prescricao)
