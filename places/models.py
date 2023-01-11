from django.db import models
from django.conf import settings
from profiles_api.models import UserProfile
# Create your models here.


class Places(models.Model):
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    spendTime = models.IntegerField()
    reviews = models.IntegerField()
    user_profile = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
     )


    def __str__(self):
        return '{}, {}'.format(self.city, self.place)
        
