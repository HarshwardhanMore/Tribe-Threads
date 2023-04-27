# Generated by Django 4.1.7 on 2023-04-26 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_vendors'),
    ]

    operations = [
        migrations.CreateModel(
            name='VendorItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.TextField()),
                ('business_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.vendors')),
            ],
        ),
    ]