from rest_framework.serializers import ModelSerializer, SerializerMethodField
from . import models


class CompanySerializer(ModelSerializer):
    class Meta:
        model = models.Company        
        fields = ('id', 'name', 'phone', 'inn')


class AdressSerializer(ModelSerializer):
    class Meta:
        model = models.Adress        
        fields = ('id', 'name', 'building_type', 'cad_number', 'company', 'companyinfo', 'votingsinfo')

    companyinfo = SerializerMethodField()
    votingsinfo = SerializerMethodField()

    def get_companyinfo(self, obj):
        return CompanySerializer().to_representation(obj.get_company())
    
    def get_votingsinfo(self, obj):
        return [VotingSerializer().to_representation(x) for x in obj.get_votings()]


class FlatSerializer(ModelSerializer):
    class Meta:
        model = models.Flat        
        fields = ('id', 'adress', 'square', 'adressinfo', 'number')

    adressinfo = SerializerMethodField()

    def get_adressinfo(self, obj):
        return AdressSerializer().to_representation(obj.get_adress())


class PersonSerializer(ModelSerializer):
    class Meta:
        model = models.Person        
        fields = ('id', 'name', 'surname', 'patronymic', 'flat', 'flatinfo', 'state', 'publick_key')

    flatinfo = SerializerMethodField()

    def get_flatinfo(self, obj):
        return FlatSerializer().to_representation(obj.get_flat())


class PersonSerializerFlat(ModelSerializer):
    class Meta:
        model = models.Person        
        fields = ('id', 'name', 'surname', 'patronymic', 'flat', 'state', 'publick_key')



class VotingSerializer(ModelSerializer):
    class Meta:
        model = models.Voting        
        fields = ('id', 'name', 'adress', 'initiator', 'initiatorinfo')

    initiatorinfo = SerializerMethodField()

    def get_initiatorinfo(self, obj):
        return PersonSerializerFlat().to_representation(obj.get_initiator())

class QuestionSerializer(ModelSerializer):
    class Meta:
        model = models.Question        
        fields = ('id', 'name', 'description', 'voting')


class AnswerSerializer(ModelSerializer):
    class Meta:
        model = models.Answer        
        fields = ('id', 'answer', 'person', 'question', 'time', 'signature')
