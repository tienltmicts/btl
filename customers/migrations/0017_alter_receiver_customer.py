# Generated by Django 3.2.4 on 2021-06-05 02:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0016_receiver_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receiver',
            name='customer',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='customers.customer'),
        ),
    ]