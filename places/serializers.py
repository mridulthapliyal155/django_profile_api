from rest_framework import serializers
from .models import Places

class PlacesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Places 
        fields = (
            'id','user_profile','country','city','place','spendTime','reviews'
        )
        extra_kwargs = {'user_profile':{'read_only':True}}