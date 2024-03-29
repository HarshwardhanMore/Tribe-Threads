# Generated by Django 4.1.7 on 2023-04-26 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_plogin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vendors',
            fields=[
                ('username', models.CharField(max_length=50)),
                ('business_name', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('primary_email', models.CharField(max_length=50)),
                ('secondary_email', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=10)),
                ('state', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('pincode', models.CharField(max_length=6)),
                ('address', models.TextField()),
                ('business_phone_number', models.CharField(max_length=10)),
                ('business_id', models.CharField(max_length=60, primary_key=True, serialize=False)),
                ('business_password', models.CharField(max_length=60)),
            ],
        ),
    ]
