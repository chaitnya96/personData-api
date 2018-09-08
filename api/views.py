# generic

from rest_framework import generics
from rest_framework.permissions import AllowAny

from .serializers import *


class PersonView(generics.ListCreateAPIView):
    queryset = PersonDetail.objects.all()
    serializer_class = PersonSerializer
    permission_classes = (AllowAny,)


class LocationView(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = (AllowAny,)
