# Generated by Django 3.0.8 on 2020-08-22 11:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zhkh', '0004_auto_20200822_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='adress',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zhkh.Flat'),
        ),
    ]
