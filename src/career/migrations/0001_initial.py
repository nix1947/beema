# Generated by Django 2.0.7 on 2018-07-26 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExamForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now=True)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('file', models.FileField(upload_to='result')),
            ],
            options={
                'verbose_name': 'Exam Form',
                'verbose_name_plural': 'Exam forms',
            },
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now=True)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('file', models.FileField(upload_to='result')),
            ],
            options={
                'verbose_name': 'Result',
                'verbose_name_plural': 'Results',
            },
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now=True)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=255)),
                ('published_in', models.CharField(blank=True, max_length=255, null=True)),
                ('body', models.TextField()),
                ('file', models.FileField(upload_to='vacancy')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]