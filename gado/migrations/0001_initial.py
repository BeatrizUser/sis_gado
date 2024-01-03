# Generated by Django 3.2.20 on 2024-01-03 04:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_identificacao', models.CharField(max_length=20)),
                ('raca', models.CharField(max_length=50)),
                ('sexo', models.CharField(max_length=10)),
                ('idade', models.IntegerField()),
                ('cor', models.CharField(max_length=20)),
                ('data_nascimento', models.DateField()),
                ('data_aquisicao', models.DateField()),
                ('data_venda_transferencia', models.DateField(blank=True, null=True)),
                ('observacoes', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'Animais',
            },
        ),
        migrations.CreateModel(
            name='RegistroSanitario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_vacinacao', models.DateField()),
                ('tipo_vacina', models.CharField(max_length=50)),
                ('tratamento_contra_parasitas', models.CharField(max_length=100)),
                ('exames_veterinarios', models.CharField(blank=True, max_length=100)),
                ('observacoes', models.TextField(blank=True)),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gado.animal')),
            ],
        ),
        migrations.CreateModel(
            name='RegistroReprodutivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_cobertura', models.DateField()),
                ('resultado_cobertura', models.CharField(max_length=20)),
                ('observacoes', models.TextField(blank=True)),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gado.animal')),
            ],
        ),
        migrations.CreateModel(
            name='RegistroAlimentacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_alimentacao', models.DateField()),
                ('tipo_alimento', models.CharField(max_length=50)),
                ('quantidade', models.FloatField()),
                ('observacoes', models.TextField(blank=True)),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gado.animal')),
            ],
        ),
    ]
