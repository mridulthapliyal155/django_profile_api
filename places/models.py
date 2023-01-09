from django.db import models
# from profiles_api import models
# Create your models here.


class Places(models.Model):
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    spendTime = models.IntegerField()
    reviews = models.IntegerField()


    def __str__(self):
        return '{}, {}'.format(self.city, self.place)
        
