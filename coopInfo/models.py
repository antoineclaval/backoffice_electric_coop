from django.db import models

class State(models.Model):
    name = models.CharField(max_length=15)

    def __unicode__(self):
        return self.name


class Cooperative(models.Model):
    stateId = models.ForeignKey(State)
    name = models.CharField(max_length=50)
    acronym = models.CharField(max_length=6)
    streetAddress = models.CharField(max_length=50)
    website = models.CharField(max_length=255, unique=True)
    mailAddress = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    countiesServed =  models.CharField(max_length=500)
    consumers = models.IntegerField(default=0)
    montlyMeeting = models.CharField(max_length=20)
    annualMeeting = models.CharField(max_length=20)
    numberOfEmployees = models.IntegerField(default=0)
    milesOfLines = models.IntegerField(default=0)
    nextElectionTerms = models.CharField(max_length=50)
    servingTime = models.CharField(max_length=50)
    bylaws = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class Person(models.Model):
    coopId = models.ForeignKey(Cooperative)
    name = models.CharField(max_length=20)
    ethnicity = models.CharField(max_length=10)
    distric = models.CharField(max_length=255)
    title = models.CharField(max_length=20)
    
    def __unicode__(self):
        return self.name