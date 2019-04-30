# Generated by Django 2.2 on 2019-04-30 13:05

import core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20190430_0853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utilitiesuser',
            name='cold_water_norm',
            field=models.FloatField(help_text='Required. Only numbers greater than zero', null=True, validators=[core.validators.validate_norm], verbose_name='Cold Water Norm'),
        ),
        migrations.AlterField(
            model_name='utilitiesuser',
            name='electricity_norm',
            field=models.FloatField(help_text='Required. Only numbers greater than zero', null=True, validators=[core.validators.validate_norm], verbose_name='Electricity Norm'),
        ),
        migrations.AlterField(
            model_name='utilitiesuser',
            name='hws_cold_water_norm',
            field=models.FloatField(help_text='Required. Only numbers greater than zero', null=True, validators=[core.validators.validate_norm], verbose_name='HWS Cold Water Norm'),
        ),
        migrations.AlterField(
            model_name='utilitiesuser',
            name='sewage_norm',
            field=models.FloatField(help_text='Required. Only numbers greater than zero', null=True, validators=[core.validators.validate_norm], verbose_name='Sewage Norm'),
        ),
    ]
