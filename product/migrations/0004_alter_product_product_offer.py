# Generated by Django 4.0.7 on 2022-10-17 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_product_product_offer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_offer',
            field=models.IntegerField(blank=True),
        ),
    ]
