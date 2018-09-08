from rest_framework import serializers

from Exam.models import PersonDetail, Location


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonDetail
        fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'
