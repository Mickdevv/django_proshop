# Generated by Django 5.0 on 2023-12-04 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_order_orderitem_review_shippingaddress'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
