from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=256)
    phone = models.CharField(max_length=256)
    inn = models.CharField(max_length=256)


class Adress(models.Model):
    name = models.CharField(max_length=256)
    building_type = models.CharField(max_length=256)
    cad_number = models.CharField(max_length=256)
    company = models.ForeignKey(Company, on_delete=models.DO_NOTHING)

    def get_company(self):
        return self.company

    def get_votings(self):
        return Voting.objects.filter(adress=self.id)


class Flat(models.Model):
    adress = models.ForeignKey(Adress, on_delete=models.CASCADE)
    square = models.IntegerField()
    number = models.IntegerField()

    def get_adress(self):
        return self.adress


class Person(models.Model):
    surname = models.CharField(max_length=256)
    name = models.CharField(max_length=256)
    patronymic = models.CharField(max_length=256)
    flat = models.ForeignKey(Flat, on_delete=models.CASCADE)
    publick_key = models.BinaryField()
    state = models.BooleanField()

    def get_flat(self):
        return self.flat


class Voting(models.Model):
    name = models.CharField(max_length=256)
    initiator = models.ForeignKey(Person, on_delete=models.CASCADE)
    adress = models.ForeignKey(Adress, on_delete=models.CASCADE)

    def get_initiator(self):
        return self.initiator

    def get_questions(self):
        return Question.objects.filter(voting=self.id)
        

class Question(models.Model):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=256)
    voting = models.ForeignKey(Voting, on_delete=models.CASCADE)

    def get_answers(self):
        return Answer.objects.filter(question=self.id)


class Answer(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    time = models.DateTimeField()
    answer = models.CharField(max_length=256)
    signature = models.BinaryField()