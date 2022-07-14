# Generated by Django 4.0.6 on 2022-07-14 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Atracao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=250)),
                ('descricao', models.TextField()),
                ('horario_funcionamento', models.CharField(max_length=250)),
                ('idade_minima', models.PositiveIntegerField()),
                ('valor', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
            options={
                'verbose_name': 'Atração',
                'verbose_name_plural': 'Atrações',
            },
        ),
    ]
