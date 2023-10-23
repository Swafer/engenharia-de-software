# Generated by Django 4.2.5 on 2023-09-18 23:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='areasaber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('area', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='avaliacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
                ('descricao', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('ementa', models.CharField(max_length=50)),
                ('carga', models.CharField(max_length=50)),
                ('duracao', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='disciplina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('ementa', models.CharField(max_length=50)),
                ('areasaber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.areasaber')),
            ],
        ),
        migrations.CreateModel(
            name='frequencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('faltas', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='horario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('periodo', models.CharField(max_length=50)),
                ('horario', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='instituicao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('site', models.CharField(max_length=50)),
                ('numero', models.CharField(max_length=50)),
                ('cidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cidade')),
            ],
        ),
        migrations.CreateModel(
            name='matricula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(max_length=50)),
                ('inicio', models.DateField()),
                ('fim', models.DateField()),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.curso')),
                ('instituição', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.instituicao')),
            ],
        ),
        migrations.CreateModel(
            name='ocorrencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('nome', models.CharField(max_length=20)),
                ('descricao', models.CharField(max_length=100)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.curso')),
                ('disciplina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.disciplina')),
            ],
        ),
        migrations.CreateModel(
            name='pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('pai', models.CharField(max_length=50)),
                ('mae', models.CharField(max_length=50)),
                ('cpf', models.CharField(max_length=50)),
                ('nascimento', models.DateField()),
                ('email', models.CharField(max_length=50)),
                ('cidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cidade')),
            ],
        ),
        migrations.CreateModel(
            name='turma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_do_curso', models.CharField(max_length=50)),
                ('cpf', models.CharField(max_length=50)),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.pessoa')),
            ],
        ),
        migrations.RemoveField(
            model_name='editora',
            name='Cidade',
        ),
        migrations.RemoveField(
            model_name='emprestimo',
            name='Leitor',
        ),
        migrations.RemoveField(
            model_name='emprestimo',
            name='Livro',
        ),
        migrations.RemoveField(
            model_name='livro',
            name='Autor',
        ),
        migrations.RemoveField(
            model_name='livro',
            name='Categoria',
        ),
        migrations.RemoveField(
            model_name='livro',
            name='Editora',
        ),
        migrations.RenameModel(
            old_name='Categoria',
            new_name='ocupacao',
        ),
        migrations.DeleteModel(
            name='Autor',
        ),
        migrations.DeleteModel(
            name='Editora',
        ),
        migrations.DeleteModel(
            name='Emprestimo',
        ),
        migrations.DeleteModel(
            name='Leitor',
        ),
        migrations.DeleteModel(
            name='Livro',
        ),
        migrations.AddField(
            model_name='pessoa',
            name='ocupacao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.ocupacao'),
        ),
        migrations.AddField(
            model_name='ocorrencia',
            name='pessoa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.pessoa'),
        ),
        migrations.AddField(
            model_name='matricula',
            name='pessoa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.pessoa'),
        ),
        migrations.AddField(
            model_name='frequencia',
            name='pessoa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.pessoa'),
        ),
        migrations.AddField(
            model_name='frequencia',
            name='turma',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.turma'),
        ),
        migrations.AddField(
            model_name='curso',
            name='disciplina',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.disciplina'),
        ),
        migrations.AddField(
            model_name='curso',
            name='instituicao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.instituicao'),
        ),
    ]