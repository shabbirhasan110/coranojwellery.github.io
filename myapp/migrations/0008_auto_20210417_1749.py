# Generated by Django 3.2 on 2021-04-17 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_remove_productmodel_p_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='discounted_price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='sell_price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]