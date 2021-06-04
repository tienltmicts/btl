# Generated by Django 3.2.4 on 2021-06-03 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idProduct', models.CharField(max_length=255, verbose_name='Mã sản phẩm')),
                ('name', models.CharField(max_length=255, verbose_name='Tên sản phẩm')),
                ('page_number', models.IntegerField(max_length=255, verbose_name='Số trang')),
                ('author', models.CharField(max_length=255, verbose_name='tác giả')),
                ('publishing_year', models.IntegerField(max_length=255, verbose_name='Năm xuất bản')),
                ('amount', models.IntegerField(default=0, verbose_name='Số lượng')),
                ('sold', models.IntegerField(blank=True, null=True, verbose_name='Đã bán')),
                ('inventory', models.IntegerField(blank=True, null=True, verbose_name='Tồn')),
                ('entry_price', models.BigIntegerField(default=0, verbose_name='Giá nhập')),
                ('added_date', models.DateTimeField(blank=True, null=True, verbose_name='Ngày nhập')),
                ('category', models.CharField(blank=True, max_length=255, null=True, verbose_name='Loại')),
                ('brand', models.CharField(default='Không thương hiệu', max_length=255, verbose_name='Thương hiệu')),
                ('origin', models.CharField(blank=True, max_length=255, null=True, verbose_name='Xuất xứ')),
            ],
            options={
                'verbose_name': 'Sách',
                'verbose_name_plural': 'Sách',
                'db_table': 'book',
            },
        ),
        migrations.CreateModel(
            name='Clothes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idProduct', models.CharField(max_length=255, verbose_name='Mã sản phẩm')),
                ('name', models.CharField(max_length=255, verbose_name='Tên sản phẩm')),
                ('color', models.CharField(max_length=255, verbose_name='Màu')),
                ('size', models.CharField(max_length=255, verbose_name='Kích cỡ')),
                ('amount', models.IntegerField(default=0, verbose_name='Số lượng')),
                ('sold', models.IntegerField(blank=True, null=True, verbose_name='Đã bán')),
                ('inventory', models.IntegerField(blank=True, null=True, verbose_name='Tồn')),
                ('entry_price', models.BigIntegerField(default=0, verbose_name='Giá nhập')),
                ('added_date', models.DateTimeField(blank=True, null=True, verbose_name='Ngày nhập')),
                ('category', models.CharField(blank=True, max_length=255, null=True, verbose_name='Loại')),
                ('brand', models.CharField(default='Không thương hiệu', max_length=255, verbose_name='Thương hiệu')),
                ('origin', models.CharField(blank=True, max_length=255, null=True, verbose_name='Xuất xứ')),
            ],
            options={
                'verbose_name': 'Quần áo',
                'verbose_name_plural': 'Quần áo',
                'db_table': 'clothes',
            },
        ),
        migrations.CreateModel(
            name='Electro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idProduct', models.CharField(max_length=255, verbose_name='Mã sản phẩm')),
                ('name', models.CharField(max_length=255, verbose_name='Tên sản phẩm')),
                ('power', models.CharField(max_length=255, verbose_name='Công suất')),
                ('amount', models.IntegerField(default=0, verbose_name='Số lượng')),
                ('sold', models.IntegerField(blank=True, null=True, verbose_name='Đã bán')),
                ('inventory', models.IntegerField(blank=True, null=True, verbose_name='Tồn')),
                ('entry_price', models.BigIntegerField(default=0, verbose_name='Giá nhập')),
                ('added_date', models.DateTimeField(blank=True, null=True, verbose_name='Ngày nhập')),
                ('category', models.CharField(blank=True, max_length=255, null=True, verbose_name='Loại')),
                ('brand', models.CharField(default='Không thương hiệu', max_length=255, verbose_name='Thương hiệu')),
                ('origin', models.CharField(blank=True, max_length=255, null=True, verbose_name='Xuất xứ')),
            ],
            options={
                'verbose_name': 'Đồ điện tử',
                'verbose_name_plural': 'Đồ điện tử',
                'db_table': 'electro',
            },
        ),
        migrations.AlterField(
            model_name='produces',
            name='inventory',
            field=models.IntegerField(blank=True, null=True, verbose_name='Tồn'),
        ),
        migrations.AlterField(
            model_name='produces',
            name='sold',
            field=models.IntegerField(blank=True, null=True, verbose_name='Đã bán'),
        ),
    ]