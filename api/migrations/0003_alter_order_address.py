# Generated by Django 5.0.4 on 2024-04-05 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_order_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(choices=[('Qibray', 'Qibray'), ('Yunsobot', 'Yunsobot'), ('Olmazor', 'Olmazor'), ('Chorsuv', 'Chorsuv'), ('Chilonzor', 'Chilonzor')], default='toshkent', max_length=250),
        ),
    ]
