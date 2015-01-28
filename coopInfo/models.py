from django.db import models


class Cooperative(models.Model):
    name = models.CharField(max_length=50)
    acronym = models.CharField(max_length=6)
    address = models.CharField(max_length=50)
    website = models.CharField(max_length=255, unique=True)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    nextElectionTerms = models.CharField(max_length=50)
    servingTime = models.CharField(max_length=50)
    annualMeeting = models.CharField(max_length=20)
    montlyMeeting = models.CharField(max_length=20)
    memberMeters = models.IntegerField(default=0)
    consumers = models.IntegerField(default=0)
    milesOfLines = models.IntegerField(default=0)
    numberOfEmployees = models.IntegerField(default=0)
    bylaws = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class Person(models.Model):
    coopId = models.ForeignKey(Cooperative)
    name = models.CharField(max_length=20)
    etnicity = models.CharField(max_length=10)
    distric = models.CharField(max_length=255)
    title = models.CharField(max_length=20)
    
    def __unicode__(self):
        return self.name
