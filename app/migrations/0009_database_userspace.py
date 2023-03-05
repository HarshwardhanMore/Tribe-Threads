# Generated by Django 3.2.16 on 2023-01-31 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0008_auto_20230201_0303'),
    ]

    operations = [
        migrations.CreateModel(
            name='Database',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=10)),
                ('price', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
                ('superCategory', models.CharField(max_length=50)),
                ('subCategories', models.CharField(max_length=300)),
                ('color', models.CharField(max_length=15)),
                ('brandName', models.CharField(max_length=25)),
                ('availableSize', models.CharField(max_length=300)),
                ('age', models.CharField(max_length=5)),
                ('season', models.CharField(max_length=10)),
                ('image', models.FileField(default=None, upload_to='productImages')),
                ('imageName', models.CharField(max_length=50)),
                ('product_id', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UserSpace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=50)),
                ('wishlist', models.CharField(max_length=5000)),
            ],
        ),
    ]
