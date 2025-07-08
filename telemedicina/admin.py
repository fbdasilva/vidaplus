from django.contrib import admin

# Register your models here.
from .models import AtendimentoOnline, PrescricaoOnline

admin.site.register(AtendimentoOnline)
admin.site.register(PrescricaoOnline)
