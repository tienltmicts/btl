# Generated by Django 3.2.4 on 2021-06-05 06:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0021_alter_payment_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='payment',
            options={'verbose_name': 'Thanh toán', 'verbose_name_plural': 'Thanh toán'},
        ),
        migrations.AlterModelTable(
            name='payment',
            table='payment',
        ),
    ]
