# Generated by Django 3.2a1 on 2021-02-19 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Repuestos', '0010_repuesto_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repuesto',
            name='codigo',
            field=models.TextField(max_length=200),
        ),
    ]
