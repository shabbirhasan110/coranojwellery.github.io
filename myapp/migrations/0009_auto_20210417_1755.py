# Generated by Django 3.2 on 2021-04-17 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_auto_20210417_1749'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productmodel',
            name='discounted_price',
        ),
        migrations.RemoveField(
            model_name='productmodel',
            name='sell_price',
        ),
    ]
