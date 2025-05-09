# Generated by Django 5.1.1 on 2025-03-24 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0022_alter_cart_totalamount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='totalamount',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='refurbishedproductmodel',
            name='status',
            field=models.CharField(choices=[('1', 'Available'), ('2', 'UnAvailable')], max_length=1, null=True),
        ),
    ]
