# Generated by Django 3.2.4 on 2021-06-04 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0011_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='receiver',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='customers.customer'),
        ),
    ]
