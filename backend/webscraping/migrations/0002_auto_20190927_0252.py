# Generated by Django 2.2.5 on 2019-09-27 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webscraping', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='date',
            field=models.DateField(),
        ),
    ]
