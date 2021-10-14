from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from mainapp.models import Token

class TokenSerializer(ModelSerializer):
    class Meta:
        model = Token
        fields = ['id', 'token', 'slug', 'isActive', 'user']
        read_only_fields = ['isActive', ]
        # lookup_field = 'slug'
        # extra_kwargs = {
        #     'url': {'lookup_field': 'slug'}
        # }