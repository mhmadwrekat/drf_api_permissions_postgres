from django.shortcuts import render
from rest_framework import generics
from .models import Thing
from.serializers import ThingSerializer
from .permissions import IsAuthenticatedOrReadOnly

# CR views
class ThingList(generics.ListCreateAPIView) :

#    queryset = Thing.objects.all()
    queryset = Thing.objects.filter(published = True)
    serializer_class = ThingSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

# RUD view
class ThingDetail(generics.RetrieveUpdateDestroyAPIView) :

    queryset = Thing.objects.all()
    serializer_class = ThingSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
