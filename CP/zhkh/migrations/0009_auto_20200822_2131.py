# Generated by Django 3.0.8 on 2020-08-22 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zhkh', '0008_auto_20200822_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='publick_key',
            field=models.CharField(max_length=2048),
        ),
    ]
