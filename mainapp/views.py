from rest_framework import serializers
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from django_filters import rest_framework as django_filter

from mainapp.models import Token
from mainapp.serializers import TokenSerializer

class TokenViewSet(ModelViewSet):
    queryset = Token.objects.all()
    serializer_class = TokenSerializer
    filter_backends = [django_filter.DjangoFilterBackend, SearchFilter]
    filter_fields = ['token', ]
    search_fields = ['token', ]


    
