# Generated by Django 3.2.7 on 2021-09-27 17:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20210927_1026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='bloc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cards', to='backend.bloc'),
        ),
    ]
