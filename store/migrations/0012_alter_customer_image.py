# Generated by Django 4.2.5 on 2023-11-30 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_alter_customer_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='image',
            field=models.ImageField(default='uploads/profile_img/pxfuel.jpg', upload_to='uploads/profile_img/'),
        ),
    ]
