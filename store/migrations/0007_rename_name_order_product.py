# Generated by Django 4.2.5 on 2023-09-27 10:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_order_address_order_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='name',
            new_name='product',
        ),
    ]
