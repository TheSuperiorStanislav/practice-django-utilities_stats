# Generated by Django 2.2.1 on 2019-06-06 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utilities', '0003_auto_20190509_0705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utilities',
            name='date',
            field=models.DateField(verbose_name='Date'),
        ),
    ]
