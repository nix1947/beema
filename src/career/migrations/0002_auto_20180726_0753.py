# Generated by Django 2.0.7 on 2018-07-26 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('career', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='examform',
            name='draft',
            field=models.BooleanField(default=True, verbose_name=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='result',
            name='draft',
            field=models.BooleanField(default=True, verbose_name=False),
            preserve_default=False,
        ),
    ]