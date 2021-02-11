# Generated by Django 3.2a1 on 2021-02-11 13:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Repuestos', '0007_remove_repuesto_marca'),
    ]

    operations = [
        migrations.AddField(
            model_name='repuesto',
            name='marca',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Repuestos.marcaauto'),
        ),
        migrations.AddField(
            model_name='repuesto',
            name='modelo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Repuestos.modelo'),
        ),
    ]
