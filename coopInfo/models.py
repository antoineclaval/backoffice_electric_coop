from django.db import models

class State(models.Model):
    name = models.CharField(max_length=15)

    def __unicode__(self):
        return self.name


class Cooperative(models.Model):
    stateId = models.ForeignKey(State)
    name = models.CharField(max_length=50)
    acronym = models.CharField(max_length=6)
    streetAddress = models.CharField(max_length=150, verbose_name='street address')
    website = models.CharField(max_length=255, unique=True)
    mailAddress = models.CharField(max_length=50, verbose_name='mail address')
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    countiesServed =  models.CharField(max_length=500, verbose_name='counties served')
    consumers = models.IntegerField(default=0, null=True, verbose_name='number of consumers')
    montlyMeeting = models.CharField(max_length=20, verbose_name='info about montly meeting')
    annualMeeting = models.CharField(max_length=20, verbose_name='info about annual meeting')
    numberOfEmployees = models.IntegerField(default=0, null=True, verbose_name='number of employees')
    milesOfLines = models.IntegerField(default=0, null=True, verbose_name='miles of electric lines')
    nextElectionTerms = models.CharField(max_length=50, verbose_name='next election')
    servingTime = models.CharField(max_length=50, verbose_name='serving time')
    bylaws = models.CharField(max_length=255)
    is990present = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name


class Person(models.Model):
    coopId = models.ForeignKey(Cooperative)
    name = models.CharField(max_length=20)
    ethnicity = models.CharField(max_length=10)
    distric = models.CharField(max_length=255)
    title = models.CharField(max_length=20)
    inBoardSince = models.DateTimeField(null=True, verbose_name='in board since')

    def __unicode__(self):
        return self.name