# Generated by Django 4.1.5 on 2023-01-04 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.IntegerField(max_length=12)),
                ('email', models.EmailField(max_length=50)),
                ('order', models.CharField(max_length=100)),
                ('date', models.DateField()),
            ],
        ),
    ]
