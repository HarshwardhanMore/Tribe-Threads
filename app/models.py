from django.db import models
from django_mysql.models import ListCharField

from numpy import random

import datetime

# Create your models here.




# ###################### BUSINESS


class Vendors(models.Model):    
    
    username = models.CharField(max_length=50)
    business_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    primary_email = models.CharField(max_length=50)
    secondary_email = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)
    # password = models.CharField(max_length=50)    
    
    state = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    pincode = models.CharField(max_length=6)
    address = models.TextField()
    business_phone_number = models.CharField(max_length=10)


    business_id = models.CharField(max_length=60, primary_key=True)
    business_password = models.CharField(max_length=60)

    def __str__(self):
        return self.first_name + "_" + self.last_name + "_" + self.phone_number
    
class VendorItems(models.Model):
    business_id = models.CharField(max_length=60)
    product_id = models.CharField(max_length=60)
    # items = models.TextField(default='[]')
    def __str__(self):
        return self.business_id

class Database(models.Model):

    # business_id = models.ForeignKey("", verbose_name=_(""), on_delete=models.CASCADE)

    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    price = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    superCategory = models.CharField(max_length=50)  # topwear, bottomwear
    # subCategories = ListCharField(
    #     base_field=models.CharField(max_length=20),
    #     size=20,
    #     max_length=(20 * 21),  # 20 * 21 character nominals, plus commas
    # )
    subCategories = models.CharField(max_length=300)
    color = models.CharField(max_length=15)
    brandName = models.CharField(max_length=25)
    # availableSize = ListCharField(
    #     base_field=models.CharField(max_length=10),
    #     size=20,
    #     max_length=(20 * 11),  # 20 * 11 character nominals, plus commas
    # )
    availableSize = models.CharField(max_length=300)
    age = models.CharField(max_length=5)
    season = models.CharField(max_length=10)
    image = models.FileField(upload_to='productImages', default=None)
    imageName = models.CharField(max_length=50)

    product_id = models.CharField(max_length=50)
    # product_id = brandName + "&&" + color + "&&" + random.rand()

    def __str__(self):
        return self.brandName + '\'s ' + self.color + ' ' + self.name + ' for ' + self.gender
    # + ' of sizes ' + '-'.join([str(elem) for elem in self.availableSize]) + ' ( ' + self.superCategory + ' ) '


# ###################### CUSTOMER

class UserSpace(models.Model):
    user_id = models.CharField(max_length=50)
    wishlist = models.TextField()
    cart = models.TextField()

    def __str__(self):
        return self.user_id




















# ###################### LOGIN

class Plogin(models.Model):
    USERNAME = models.CharField(max_length=20)
    PASSWORD = models.CharField(max_length=20)
    date = models.DateField(default=datetime.datetime.now)

    def __str__(self):
        return self.USERNAME
