# Generated by Django 3.2.4 on 2021-07-03 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=200)),
                ('mobile_number', models.CharField(max_length=50, unique=True)),
                ('nickname', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
