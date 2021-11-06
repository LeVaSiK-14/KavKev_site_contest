from rest_framework import serializers
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.filters import SearchFilter
from django_filters import rest_framework as django_filter
from rest_framework.response import Response

from mainapp.models import Token
from mainapp.serializers import TokenSerializer

class ListCreateToken(ListCreateAPIView):
    queryset = Token.objects.all()
    serializer_class = TokenSerializer
    filter_backends = [django_filter.DjangoFilterBackend, SearchFilter]
    filter_fields = ['token', ]
    search_fields = ['token', ]
    


class RetrieveUpdateToken(RetrieveUpdateAPIView):
    queryset = Token.objects.all()
    serializer_class = TokenSerializer
    lookup_field = 'slug'


    def update(self, request, *args, **kwargs):
        token = self.get_object()
        user = request.user
        if token.isActive == False:
            return Response({'Error': 'Данный QR код был отсканирован ранее'})
        else:
            token.user = user
            token.isActive = False
            token.save()
            user.qr_quantity += 1
            user.save()
            if user.qr_quantity >= 5:
                user.which_contest = "MORE_5_LESS_10"
                user.save()
                return Response({"Success": f"Поздравляем вы учавствуете в маленьком конкурсе! {user.qr_quantity}"})
            elif user.qr_quantity >= 10:
                user.which_contest = "MORE_10_LESS_100"
                user.save()
                return Response({"Success": f"Поздравляем вы учавствуете в среднем конкурсе! {user.qr_quantity}"})
            elif user.qr_quantity >= 100:
                user.which_contest = "MORE_100"
                user.save()
                return Response({"Success": f"Поздравляем вы учавствуете в самом большом конкурсе! {user.qr_quantity}"})
            else:
                user.which_contest = "LESS_5"
                user.save()
                return Response({"Success": f"Отсканируйте больше 5 Qr кодов, что бы начать учавствовать в конкурсе! {user.qr_quantity}"})
            
    # serializer = TokenSerializer(instance=token)
    # return Response(serializer.data)
