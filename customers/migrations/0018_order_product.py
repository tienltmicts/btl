# Generated by Django 3.2.4 on 2021-06-05 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0017_alter_receiver_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.TextField(blank=True, null=True),
        ),
    ]
