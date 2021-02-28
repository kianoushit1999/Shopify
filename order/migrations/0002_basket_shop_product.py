# Generated by Django 3.1.6 on 2021-02-28 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_auto_20210222_1759'),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='basket',
            name='shop_product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='basket_shop_product', related_query_name='basket_shop_product', to='product.shopproduct'),
        ),
    ]
