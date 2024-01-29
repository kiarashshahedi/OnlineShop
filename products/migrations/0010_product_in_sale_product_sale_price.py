# Generated by Django 5.0.1 on 2024-01-29 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_alter_order_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='in_sale',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='sale_price',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=9),
        ),
    ]
