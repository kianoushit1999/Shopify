# Generated by Django 3.1.6 on 2021-02-28 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20210228_1538'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='order',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='user',
        ),
        migrations.RemoveField(
            model_name='table',
            name='order',
        ),
        migrations.RemoveField(
            model_name='table',
            name='shop_product',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='payment',
        ),
        migrations.DeleteModel(
            name='Table',
        ),
    ]
