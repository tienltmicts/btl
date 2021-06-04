from django.db import models

from warehouse.models import *

# Create your models here.
class ItemClothes(models.Model):
    produce = models.OneToOneField(Clothes,  null=True, blank=True, on_delete=models.CASCADE)
    image = models.ImageField(('Ảnh sản phẩm'),upload_to="media/produce",default = 'media/produce/None/no-img.jpg')
    sale_off = models.IntegerField("Khuyến mãi", default=0)
    price = models.BigIntegerField("Giá bán", default=0)
    describe = models.TextField("Mô tả",)

    class Meta:
        db_table ="item_clothes"
        verbose_name = "Sản phẩm quần áo"
        verbose_name_plural = "Sản phẩm quần áo"
    
    def __str__(self):
        return self.produce.name
    
class ItemElectro(models.Model):
    produce = models.OneToOneField(Electro,  null=True, blank=True, on_delete=models.CASCADE)
    image = models.ImageField(('Ảnh sản phẩm'),upload_to="media/produce",default = 'media/produce/None/no-img.jpg')
    sale_off = models.IntegerField("Khuyến mãi", default=0)
    price = models.BigIntegerField("Giá bán", default=0)
    describe = models.TextField("Mô tả",)

    class Meta:
        db_table ="item_electro"
        verbose_name = "Sản phẩm điện tử"
        verbose_name_plural = "Sản phẩm điện tử"
    
    def __str__(self):
        return self.produce.name
    
class ItemBook(models.Model):
    produce = models.OneToOneField(Book,  null=True, blank=True, on_delete=models.CASCADE)
    image = models.ImageField(('Ảnh sản phẩm'),upload_to="media/produce",default = 'media/produce/None/no-img.jpg')
    sale_off = models.IntegerField("Khuyến mãi", default=0)
    price = models.BigIntegerField("Giá bán", default=0)
    describe = models.TextField("Mô tả",)

    class Meta:
        db_table ="item_book"
        verbose_name = "Sản phẩm sách"
        verbose_name_plural = "Sản phẩm sách"
    
    def __str__(self):
        return self.produce.name