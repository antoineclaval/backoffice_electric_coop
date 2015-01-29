from django.shortcuts import render
from coopInfo.models import Person
from coopInfo.serializers import PersonSerializer
from rest_framework import generics


class PersonList(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer