# Generated by Django 3.0.8 on 2020-08-22 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zhkh', '0006_auto_20200822_1559'),
    ]

    operations = [
        migrations.AddField(
            model_name='flat',
            name='number',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
