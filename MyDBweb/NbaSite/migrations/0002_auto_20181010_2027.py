# Generated by Django 2.1.2 on 2018-10-10 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NbaSite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='begin_date',
            field=models.DateField(verbose_name='date attend'),
        ),
    ]