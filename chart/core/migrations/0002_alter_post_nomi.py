# Generated by Django 4.0 on 2022-04-18 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='nomi',
            field=models.TextField(),
        ),
    ]