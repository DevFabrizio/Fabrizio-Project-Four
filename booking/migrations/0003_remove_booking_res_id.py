# Generated by Django 3.2.19 on 2023-06-20 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_remove_customer_customer_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='res_id',
        ),
    ]
