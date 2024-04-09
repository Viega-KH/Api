# Generated by Django 5.0.4 on 2024-04-05 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
                ('phone_number', models.CharField(max_length=13)),
                ('address', models.CharField(choices=[('toshkent', 'TOSHKENT'), ('jizzax', 'JIZZAX')], default='toshkent', max_length=250)),
                ('liters', models.CharField(max_length=10)),
                ('date', models.DateField(auto_now_add=True)),
                ('time', models.TimeField(auto_now_add=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]