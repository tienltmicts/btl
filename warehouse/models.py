from django.db import models

# Create your models here.

# class Warehouse(models):
#     class Meta:
#         db_table = "warehouse"
#         verbose_name = 'Kho'
#         verbose_name_plural = 'kho'
        
#     def __str__(self):
#         return self.name

class Clothes(models.Model):
    idProduct = models.CharField("Mã sản phẩm", max_length=255)
    name = models.CharField("Tên sản phẩm",max_length=255)
    color = models.CharField("Màu",max_length=255)
    size = models.CharField("Kích cỡ",max_length=255)
    amount = models.IntegerField("Số lượng",default=0)
    sold = models.IntegerField("Đã bán", null=True, blank=True)
    inventory = models.IntegerField("Tồn", null=True, blank=True)
    entry_price = models.BigIntegerField("Giá nhập", default=0)
    added_date = models.DateTimeField("Ngày nhập", null=True, blank=True)
    category = models.CharField("Loại", max_length=255, null=True, blank=True)
    brand = models.CharField("Thương hiệu", max_length=255, default="Không thương hiệu")
    origin = models.CharField("Xuất xứ", max_length=255, null=True, blank=True)
    class Meta:
        db_table = "clothes"
        verbose_name = 'Quần áo'
        verbose_name_plural = 'Quần áo'
        
    def __str__(self):
        return self.name
    
class Electro(models.Model):
    idProduct = models.CharField("Mã sản phẩm", max_length=255)
    name = models.CharField("Tên sản phẩm",max_length=255)
    power = models.CharField("Công suất",max_length=255)
    amount = models.IntegerField("Số lượng",default=0)
    sold = models.IntegerField("Đã bán", null=True, blank=True)
    inventory = models.IntegerField("Tồn", null=True, blank=True)
    entry_price = models.BigIntegerField("Giá nhập", default=0)
    added_date = models.DateTimeField("Ngày nhập", null=True, blank=True)
    category = models.CharField("Loại", max_length=255, null=True, blank=True)
    brand = models.CharField("Thương hiệu", max_length=255, default="Không thương hiệu")
    origin = models.CharField("Xuất xứ", max_length=255, null=True, blank=True)
    class Meta:
        db_table = "electro"
        verbose_name = 'Đồ điện tử'
        verbose_name_plural = 'Đồ điện tử'
        
    def __str__(self):
        return self.name
    
class Book(models.Model):
    idProduct = models.CharField("Mã sản phẩm", max_length=255)
    name = models.CharField("Tên sản phẩm",max_length=255)
    page_number = models.IntegerField("Số trang", max_length=255)
    author = models.CharField("tác giả",max_length=255)
    publishing_year = models.IntegerField("Năm xuất bản", max_length=255)
    amount = models.IntegerField("Số lượng",default=0)
    sold = models.IntegerField("Đã bán", null=True, blank=True)
    inventory = models.IntegerField("Tồn", null=True, blank=True)
    entry_price = models.BigIntegerField("Giá nhập", default=0)
    added_date = models.DateTimeField("Ngày nhập", null=True, blank=True)
    category = models.CharField("Loại", max_length=255, null=True, blank=True)
    brand = models.CharField("Thương hiệu", max_length=255, default="Không thương hiệu")
    origin = models.CharField("Xuất xứ", max_length=255, null=True, blank=True)
    class Meta:
        db_table = "book"
        verbose_name = 'Sách'
        verbose_name_plural = 'Sách'
        
    def __str__(self):
        return self.name