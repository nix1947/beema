# Generated by Django 2.0.7 on 2018-07-26 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('career', '0002_auto_20180726_0753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examform',
            name='draft',
            field=models.BooleanField(default=False, verbose_name='Draft'),
        ),
        migrations.AlterField(
            model_name='result',
            name='draft',
            field=models.BooleanField(default=False, verbose_name='Draft'),
        ),
    ]
