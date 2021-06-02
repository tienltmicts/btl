from django.db import models

# Create your models here.
class Produces(models.Model):
    idProduce = models.CharField("Mã sản phẩm", max_length=255)
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
        db_table = "produce"
        verbose_name = 'Mặt hàng'
        verbose_name_plural = 'Mặt hàng'
        
    def __str__(self):
        return self.name