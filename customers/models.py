from django.db import models
from django.contrib.auth.models import User

# Create your models here.
USER_PROFILE_GENDER_CHOICES = [
        (0, 'Khác'),
        (1, 'Nam'),
        (2, 'Nữ'),
    ]
class Customer(models.Model):
    class Meta:
        db_table = "customer"
        verbose_name = 'Customer'
        verbose_name_plural = 'Customer'
    uid = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    birthday = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=255)
    gender = models.PositiveSmallIntegerField(('Gender'), choices=USER_PROFILE_GENDER_CHOICES, default=0)
    id_selfie = models.ImageField(('Selfie'),upload_to="media/profile",default = 'media/profile/1.jpg')

    class Meta:
        db_table = "customer"
        verbose_name = 'Customer'
        verbose_name_plural = 'Customer'