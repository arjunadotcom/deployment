# Generated by Django 4.1.1 on 2022-09-19 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='images',
            field=models.ImageField(upload_to='pics/products'),
        ),
        migrations.AlterField(
            model_name='product',
            name='images1',
            field=models.ImageField(upload_to='pics/products'),
        ),
        migrations.AlterField(
            model_name='product',
            name='images2',
            field=models.ImageField(upload_to='pics/products'),
        ),
    ]
