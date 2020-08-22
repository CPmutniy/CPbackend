from rest_framework.serializers import ModelSerializer, SerializerMethodField
from . import models

class CompanySerializer(ModelSerializer):
    class Meta:
        model = models.Company        
        fields = ('name', 'id')