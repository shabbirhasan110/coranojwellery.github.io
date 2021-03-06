# Generated by Django 3.2 on 2021-04-16 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('main_cate', models.CharField(choices=[('Men', 'Men'), ('Women', 'Women'), ('Kids', 'Kids')], max_length=200)),
                ('sub_cate', models.CharField(choices=[('Anklet', 'Anklet'), ('Barrette', 'Barrette'), ('Belt buckle', 'Belt buckle'), ('Belly chain', 'Belly chain'), ('Bindi', 'Bindi'), ('Bolo tie', 'Bolo tie'), ('Bracelet', 'Bracelet'), ('Brooch', 'Brooch'), ('Earrings', 'Earrings'), ('Ear cuff', 'Ear cuff'), ('Fascinator', 'Fascinator'), ('Hairpin', 'Hairpin'), ('Hatpin', 'Hatpin')], max_length=200)),
                ('og_price', models.IntegerField()),
                ('discount', models.IntegerField()),
                ('discounted_price', models.IntegerField()),
                ('sell_price', models.IntegerField()),
                ('p_material', models.CharField(choices=[('Gold', 'Gold'), ('Silver', 'Silver'), ('Platinum', 'Platimnum'), ('Brass', 'Brass'), ('Diamond', 'Diamond')], max_length=200)),
                ('p_brand', models.CharField(choices=[('Tanishq', 'Tanishq'), ('TBZ', 'TBZ'), ('Malabar', 'Malabar'), ('Kalyan', 'Kalyan'), ('Bhima', 'Bhima')], max_length=200)),
                ('p_occasion', models.CharField(choices=[('Birthday', 'Birthday'), ('Marriage Anniversary', 'Marriage Anniversary'), ('Engagement', 'Engagement'), ('Partywear', 'Partywear'), ('Alltime', 'Alltime')], max_length=200)),
                ('p_des', models.TextField()),
            ],
        ),
    ]
