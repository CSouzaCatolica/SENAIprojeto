# Generated by Django 5.1.7 on 2025-04-07 00:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cargos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('img_ref', models.CharField(blank=True, max_length=255, null=True)),
                ('quantidade', models.IntegerField()),
                ('d_vencimento', models.DateField(blank=True, null=True)),
                ('status', models.BooleanField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Estoque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.BigIntegerField()),
                ('deleted', models.BooleanField(default=0)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='estoques', to='app_home.item')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('senha', models.CharField(max_length=255)),
                ('d_admissao', models.DateField()),
                ('d_demissao', models.DateField(blank=True, null=True)),
                ('status', models.BooleanField(default=1)),
                ('cargo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='usuarios', to='app_home.cargos')),
            ],
        ),
        migrations.CreateModel(
            name='Emprestimo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('d_emprestimo', models.DateField()),
                ('d_devolucao', models.DateField()),
                ('d_devolvido', models.DateField(blank=True, null=True)),
                ('quantidade', models.IntegerField()),
                ('status', models.BooleanField(default=1)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emprestimos', to='app_home.item')),
                ('destinatario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emprestimos_recebidos', to='app_home.usuario')),
                ('solicitante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emprestimos_feitos', to='app_home.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=64, unique=True)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('expira_em', models.DateTimeField()),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app_home.usuario')),
            ],
        ),
    ]
