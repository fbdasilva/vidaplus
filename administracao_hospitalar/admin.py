from django.contrib import admin

# Register your models here.
from .models import Leito, Suprimento, RelatorioFinanceiro

admin.site.register(Leito)
admin.site.register(Suprimento)
admin.site.register(RelatorioFinanceiro)
