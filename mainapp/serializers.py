from rest_framework.serializers import ModelSerializer
from mainapp.models import Token

class TokenSerializer(ModelSerializer):
    class Meta:
        model = Token
        fields = ['id', 'token', 'isActive']
        read_only_fields = ['isActive', ]