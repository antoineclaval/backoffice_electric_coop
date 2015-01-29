from django.forms import widgets
from rest_framework import serializers
from coopInfo.models import Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 'coopId', 'name', 'ethnicity', 'distric', 'title', 'inBoardSince')