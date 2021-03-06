# Generated by Django 3.1.6 on 2021-02-28 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_basket_shop_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basket',
            name='shop_product',
        ),
        migrations.RemoveField(
            model_name='basketitems',
            name='basket',
        ),
        migrations.AddField(
            model_name='basket',
            name='basket_items',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='basket_basket_items', related_query_name='basket_basket_items', to='order.basketitems'),
        ),
        migrations.AddField(
            model_name='basketitems',
            name='counter',
            field=models.IntegerField(default=True, null=True),
        ),
    ]
