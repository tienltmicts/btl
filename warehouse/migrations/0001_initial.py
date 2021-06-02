# Generated by Django 3.2.4 on 2021-06-02 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produces',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idProduce', models.CharField(max_length=255, verbose_name='Mã sản phẩm')),
                ('name', models.CharField(max_length=255, verbose_name='Tên sản phẩm')),
                ('color', models.CharField(max_length=255, verbose_name='Màu')),
                ('size', models.CharField(max_length=255, verbose_name='Kích cỡ')),
                ('amount', models.IntegerField(default=0, verbose_name='Số lượng')),
                ('sold', models.IntegerField(default=0, verbose_name='Đã bán')),
                ('inventory', models.IntegerField(default=0, verbose_name='Tồn')),
                ('entry_price', models.BigIntegerField(default=0, verbose_name='Giá nhập')),
                ('added_date', models.DateTimeField(blank=True, null=True, verbose_name='Ngày nhập')),
                ('category', models.CharField(blank=True, max_length=255, null=True, verbose_name='Loại')),
                ('brand', models.CharField(default='Không thương hiệu', max_length=255, verbose_name='Thương hiệu')),
                ('origin', models.CharField(blank=True, max_length=255, null=True, verbose_name='Xuất xứ')),
            ],
            options={
                'verbose_name': 'Mặt hàng',
                'verbose_name_plural': 'Mặt hàng',
                'db_table': 'produce',
            },
        ),
    ]
