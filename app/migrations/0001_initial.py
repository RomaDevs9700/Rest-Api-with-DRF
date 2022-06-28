# Generated by Django 3.2.9 on 2022-05-01 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Talaba',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=300)),
                ('faculties', models.CharField(max_length=300)),
                ('direction', models.CharField(max_length=300)),
                ('stage', models.IntegerField(max_length=2)),
                ('group', models.IntegerField(max_length=10)),
            ],
        ),
    ]
