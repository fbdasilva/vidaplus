# Generated by Django 5.2.4 on 2025-07-07 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profissionais', '0003_prescricao'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescricao',
            name='data',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='prescricao',
            name='observacoes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='prescricao',
            name='medicamento',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
