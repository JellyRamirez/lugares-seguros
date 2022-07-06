from django.db import models

# Create your models here.

class Place(models.Model):

    name = models.CharField(max_length=256)
    description = models.CharField(max_length=256)
    address_state = models.CharField(max_length=32)
    address_city = models.CharField(max_length=32)
    address_suburb = models.CharField(max_length=32)
    address_street = models.CharField(max_length=32)
    address_zipcode = models.CharField(max_length=32)

    class Meta:
        db_table = 'places'

    def __str__(self) :
        return self.name