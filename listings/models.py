from django.db import models
from datetime import datetime
from realtors.models import Realtor  # models.py under Realtors app
from . import choices

district_list = [(key, value)
                 for key, value in choices.district_choices.items()]  # comprehension list


'''
from uuid import uuid4
import os

def path_and_rename(instance, filename):
    upload_to = 'photos/{%Y}/{%m}/{%d}'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)
'''


class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)  # Character Field
    address = models.CharField(max_length=200)
    district = models.CharField(max_length=100, choices=district_list)
    description = models.TextField(blank=True)  # Text Field
    price = models.IntegerField()  # Integer Field
    bedrooms = models.IntegerField()
    sqft = models.IntegerField()  # Integer Field
    # Decimal and float are different. Floats are approximation based on binary number system. Decimals are based on base 10 number system.
    lot_size = models.DecimalField(max_digits=2, decimal_places=1)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d')
    # This makes it so that year, month and day each have a subfolder
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    is_published = models.BooleanField(default=True)  # True or False Field
    list_date = models.DateTimeField(
        default=datetime.now, blank=True)  # Date and Time Field

    def get_district_display(self):
        return dict(choices.district_choices).get(self.district, '')

    def __str__(self):
        # Return the names of the respective data in the database
        return f"House Title : {self.title}"

# Create your models here.
