# Generated by Django 4.1 on 2023-05-07 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_category_orderid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='photo_url',
            field=models.CharField(blank=True, max_length=3000, null=True),
        ),
    ]
