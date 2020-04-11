# Generated by Django 3.0.5 on 2020-04-09 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('fileImport', models.FileField(upload_to='')),
                ('column_labels', models.TextField(blank=True)),
            ],
        ),
    ]
