# Generated by Django 5.1.3 on 2024-11-23 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_book_stock_quantity_alter_book_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(default='0000000000', max_length=15),
        ),
        migrations.AddField(
            model_name='order',
            name='transaction_id',
            field=models.CharField(default=0, max_length=255),
        ),
    ]
