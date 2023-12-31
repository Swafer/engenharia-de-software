# Generated by Django 4.2.7 on 2023-11-07 00:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='carro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idcarro', models.CharField(max_length=3)),
                ('data_entrada', models.DateField(max_length=3)),
                ('data_saida', models.DateField(max_length=3)),
                ('cor', models.CharField(max_length=50)),
                ('placa', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idcategoria', models.CharField(max_length=3)),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idmarca', models.CharField(max_length=3)),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='modelo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idmodelo', models.CharField(max_length=3)),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idpessoa', models.CharField(max_length=3)),
                ('nome', models.CharField(max_length=50)),
                ('tipo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='vagas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idvaga', models.CharField(max_length=3)),
                ('lvaga', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='reparo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idmodelo', models.CharField(max_length=3)),
                ('nome', models.CharField(max_length=50)),
                ('mecanico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.pessoa')),
                ('veiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.carro')),
            ],
        ),
    ]
