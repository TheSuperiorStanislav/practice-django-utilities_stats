# Generated by Django 2.2.1 on 2019-05-09 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20190509_0446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utilitiesuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='email address'),
        ),
    ]
