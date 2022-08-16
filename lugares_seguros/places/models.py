from django.db import models

# Create your models here.
def upload_img(instance, filename):
    return f'imgs_places/{instance.name}/{filename}'

class Place(models.Model):

    name = models.CharField(max_length=256)
    description = models.CharField(max_length=256)
    address_state = models.CharField(max_length=32)
    address_city = models.CharField(max_length=32)
    address_suburb = models.CharField(max_length=32)
    address_street = models.CharField(max_length=32)
    address_zipcode = models.CharField(max_length=32)
    image = models.ImageField(upload_to=upload_img, default='default.png', null=False)
    
    class Meta:
        db_table = 'places'

    def __str__(self) :
        return self.name