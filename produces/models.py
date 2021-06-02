from django.db import models

from warehouse.models import *

# Create your models here.
class Item(models.Model):
    produce = models.OneToOneField(Produces,  null=True, blank=True, on_delete=models.CASCADE)
    image = models.ImageField(('Ảnh sản phẩm'),upload_to="media/produce",default = 'media/produce/None/no-img.jpg')
    sale_off = models.IntegerField("Khuyến mãi", default=0)
    price = models.BigIntegerField("Giá bán", default=0)
    describe = models.TextField("Mô tả",)

    class Meta:
        db_table ="item"
        verbose_name = "Sản phẩm"
        verbose_name_plural = "Sản phẩm"
    
    def __str__(self):
        return self.produce.name