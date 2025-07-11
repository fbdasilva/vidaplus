# Generated by Django 5.2.4 on 2025-07-08 00:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0002_remove_consulta_motivo_remove_exame_resultado_and_more'),
        ('profissionais', '0004_prescricao_data_prescricao_observacoes_and_more'),
        ('telemedicina', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescricaoonline',
            name='observacoes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='VideoChamada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(auto_now_add=True)),
                ('medico', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='profissionais.medico')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pacientes.paciente')),
            ],
        ),
    ]
