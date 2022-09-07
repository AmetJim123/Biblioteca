# Generated by Django 4.1 on 2022-09-05 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='libro',
            name='portada',
        ),
        migrations.RemoveField(
            model_name='libro',
            name='categoria',
        ),
        migrations.AddField(
            model_name='libro',
            name='categoria',
            field=models.ManyToManyField(to='libro.categoria'),
        ),
    ]
