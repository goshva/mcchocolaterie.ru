from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Category(models.Model):
    name= models.CharField(max_length=50)
    orderid= models.IntegerField(validators=[ MaxValueValidator(100), MinValueValidator(1)], default=1, blank=True, null=True)

    @staticmethod
    def get_all_categories():
        return Category.objects.all().order_by('orderid')

    def __str__(self):
        return self.name
