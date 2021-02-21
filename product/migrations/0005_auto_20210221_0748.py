# Generated by Django 3.1.6 on 2021-02-21 07:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20210221_0743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopproduct',
            name='shop',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shop_product_shop', related_query_name='shop_product_shop', to='product.shop', verbose_name='shop'),
        ),
    ]