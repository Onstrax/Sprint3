# Generated by Django 3.2.6 on 2024-10-08 04:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('instituciones', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recibo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('fecha', models.DateField(auto_now=True)),
                ('valor', models.FloatField(default=0)),
                ('tipo', models.CharField(choices=[('Cobro', 'Cobro'), ('Pago', 'Pago')], max_length=100)),
                ('estado', models.CharField(choices=[('Generado', 'Generado'), ('Pagado', 'Pagado')], max_length=100)),
                ('institucion', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='instituciones.institucion')),
            ],
        ),
    ]
