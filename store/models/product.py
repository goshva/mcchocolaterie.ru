from django.conf import settings
from django.utils import timezone
from django.db import models
from django.utils.html import mark_safe
from .category import Category
class Products(models.Model):
    name = models.CharField(max_length=260, blank=True, null=True)
    price= models.IntegerField(default=0, blank=True, null=True)
    price_5k = models.FloatField(blank=True,null=True)
    price_10k = models.FloatField(blank=True,null=True)
    price_20k = models.FloatField(blank=True,null=True)
    price_many = models.FloatField(blank=True,null=True)
    kind = models.CharField(max_length=300, blank=True, null=True)
    category= models.ForeignKey(Category,on_delete=models.CASCADE,default=1, blank=True, null=True )
    description= models.CharField(max_length=250, default='', blank=True, null= True)
    photo_url = models.CharField(max_length=3000,null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=300, blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    article = models.CharField(max_length=20, blank=True, null=True)
    color = models.CharField(max_length=250, blank=True, null=True)
    size = models.FloatField(blank=True,null=True)
    weight = models.FloatField(blank=True,null=True)
    created_date = models.DateTimeField(default=timezone.now, blank=True, null=True)
    published_date = models.DateTimeField(blank=True, null=True)
    image= models.ImageField(upload_to='uploads/products/', blank=True, null=True)

    @property
    def thumbnail_preview(self):
        if self.image:
            return mark_safe('<img src="{}" width="300" height="300" />'.format(self.image.url))
        return ""

    @staticmethod
    def get_products_by_id(ids):
        return Products.objects.filter (id__in=ids)
    @staticmethod
    def get_all_products():
        return Products.objects.all().exclude(image='') #только с каринками

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Products.objects.filter (category=category_id)
        else:
            return Products.get_all_products();

