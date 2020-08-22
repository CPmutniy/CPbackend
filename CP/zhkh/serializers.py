from rest_framework.serializers import ModelSerializer, SerializerMethodField
from . import models

class CompanySerializer(ModelSerializer):
    class Meta:
        model = models.Company        
        fields = ('name', 'id')


class AdressSerializer(ModelSerializer):
    class Meta:
        model = models.Adress        
        fields = ('name', 'id')


class PersonSerializer(ModelSerializer):
    class Meta:
        model = models.Person        
        fields = ('name', 'id')


class VotingSerializer(ModelSerializer):
    class Meta:
        model = models.Voting        
        fields = ('name', 'id')


class QuestionSerializer(ModelSerializer):
    class Meta:
        model = models.Question        
        fields = ('name', 'id')


class AnswerSerializer(ModelSerializer):
    class Meta:
        model = models.Answer        
        fields = ('answer', 'id')
