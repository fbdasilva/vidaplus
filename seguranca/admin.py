from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import PerfilUsuario, RegistroAuditoria

admin.site.register(PerfilUsuario)
admin.site.register(RegistroAuditoria)
