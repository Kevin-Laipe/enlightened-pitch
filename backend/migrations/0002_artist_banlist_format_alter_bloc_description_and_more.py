# Generated by Django 4.0.4 on 2022-05-08 19:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('portfolio', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Banlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isBannedInClassicConstructed', models.BooleanField(default=True)),
                ('isBannedInBlitz', models.BooleanField(default=True)),
                ('isBannedInCommoner', models.BooleanField(default=True)),
                ('isBannedInUltimatePitFight', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Format',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='bloc',
            name='description',
            field=models.TextField(max_length=500),
        ),
        migrations.AddConstraint(
            model_name='format',
            constraint=models.UniqueConstraint(fields=('name',), name='unique format'),
        ),
        migrations.AddField(
            model_name='banlist',
            name='card',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='banned', to='backend.card'),
        ),
        migrations.AddField(
            model_name='deck',
            name='format',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.format'),
        ),
        migrations.AddField(
            model_name='image',
            name='artist',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.artist'),
        ),
    ]
