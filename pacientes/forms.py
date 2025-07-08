from django import forms
from .models import Paciente

from django import forms
from .models import Paciente, Consulta, Exame, Prontuario

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nome', 'cpf', 'data_nascimento', 'historico_clinico']
        widgets = {
            'data_nascimento': forms.DateInput(attrs={'type': 'date'}),
            'historico_clinico': forms.Textarea(attrs={'rows': 4}),
        }


class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ['paciente', 'data', 'resumo', 'medico', 'unidade']
        widgets = {
            'data': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }


class ExameForm(forms.ModelForm):
    class Meta:
        model = Exame
        fields = ['paciente', 'resumo', 'data', 'unidade']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
        }


class ProntuarioForm(forms.ModelForm):
    class Meta:
        model = Prontuario
        fields = ['paciente', 'historico', 'consultas', 'exames']
        widgets = {
            'historico': forms.Textarea(attrs={'rows': 5}),
            'consultas': forms.CheckboxSelectMultiple(),
            'exames': forms.CheckboxSelectMultiple(),
        }
