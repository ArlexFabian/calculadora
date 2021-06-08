#from django.contrib.auth.models import User, Group
from ..models import Getoperacion
from rest_framework import serializers



class OpeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Getoperacion
        fields = ['id','operacion']
    

    


