# Generated by Django 4.1.7 on 2023-04-26 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_delete_vendoritems'),
    ]

    operations = [
        migrations.CreateModel(
            name='VendorItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_id', models.CharField(max_length=60)),
                ('product_id', models.CharField(max_length=60)),
            ],
        ),
    ]
