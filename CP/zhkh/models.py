from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=256)


class Adress(models.Model):
    name = models.CharField(max_length=256)
    company = models.ForeignKey(Company, on_delete=models.DO_NOTHING)


class Person(models.Model):
    surname = models.CharField(max_length=256)
    name = models.CharField(max_length=256)
    patronymic = models.CharField(max_length=256)
    adress = models.ForeignKey(Adress, on_delete=models.CASCADE)
    publick_key = models.BinaryField()


class Voting(models.Model):
    name = models.CharField(max_length=256)


class Question(models.Model):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=256)


class Answer(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    time = models.DateTimeField()
    answer = models.CharField(max_length=256)
    signature = models.BinaryField()