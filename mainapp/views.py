from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.filters import SearchFilter
from django_filters import rest_framework as django_filter
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from mainapp.models import Token
from mainapp.serializers import TokenSerializer
from accounts.models import Contest


class ListCreateToken(ListCreateAPIView):
    queryset = Token.objects.all()
    serializer_class = TokenSerializer
    permission_classes = [IsAdminUser, ]
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
            if user.qr_in_day >= 3:
                return Response({'Error': 'В день можно отсканировать не более 3 QR кодов'})
            else:

                token.user = user
                token.isActive = False
                token.save()
                user.qr_quantity += 1
                user.qr_in_day += 1
                user.save()

                contests = Contest.objects.all().order_by('need_qr')
                print(contests)
                if user.qr_quantity < contests.first().need_qr:
                    return Response({
                                    "Success": 
                                    f"Отсканируйте больше {contests.first().need_qr} Qr кодов, что бы начать учавствовать в конкурсе! {contests.first().name_contest}"})
                elif user.qr_quantity >= contests.last().need_qr:
                    return Response({"Success": f"Поздравляем вы учавствуете в самом большом конкурсе на !{contests.last().name_contest}"})
                else:
                    for i in range(1, len(contests)):
                        if user.qr_quantity >= contests[i-1].need_qr and user.qr_quantity < contests[i].need_qr:
                            return Response({"Success": f"Поздравляем вы учавствуете в конкурсе номер {contests[i-1].need_qr}! {user.qr_quantity}"})