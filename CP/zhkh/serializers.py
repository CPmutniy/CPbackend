from rest_framework.serializers import ModelSerializer, SerializerMethodField
from . import models


class CompanySerializer(ModelSerializer):
    class Meta:
        model = models.Company        
        fields = ('id', 'name', 'phone', 'inn')


class AdressSerializer(ModelSerializer):
    class Meta:
        model = models.Adress        
        fields = ('id', 'name', 'building_type', 'cad_number', 'company')


class PersonSerializer(ModelSerializer):
    class Meta:
        model = models.Person        
        fields = ('id', 'name', 'surname', 'patronymic', 'adress', 'state', 'publick_key')


class VotingSerializer(ModelSerializer):
    class Meta:
        model = models.Voting        
        fields = ('id', 'name', 'adress')


class QuestionSerializer(ModelSerializer):
    class Meta:
        model = models.Question        
        fields = ('id', 'name', 'description', 'voting')


class AnswerSerializer(ModelSerializer):
    class Meta:
        model = models.Answer        
        fields = ('id', 'answer', 'person', 'question', 'time', 'signature')
