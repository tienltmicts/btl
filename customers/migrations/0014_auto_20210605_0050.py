# Generated by Django 3.2.4 on 2021-06-04 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0013_auto_20210605_0042'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='books',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='clothes',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='electros',
        ),
        migrations.AddField(
            model_name='cart',
            name='nameCart',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
