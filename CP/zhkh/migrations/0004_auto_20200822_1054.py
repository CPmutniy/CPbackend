# Generated by Django 3.0.8 on 2020-08-22 10:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zhkh', '0003_auto_20200822_0656'),
    ]

    operations = [
        migrations.AddField(
            model_name='voting',
            name='adress',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='zhkh.Adress'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='voting',
            name='initiator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='zhkh.Person'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Flat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('square', models.IntegerField()),
                ('adress', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zhkh.Adress')),
            ],
        ),
    ]