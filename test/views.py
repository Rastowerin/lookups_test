from rest_framework import viewsets
from .serializers import MtmFirstSerializer, MtmSecondSerializer, MtoSerializer
from .models import MtmFirst, MtmSecond, Mto


class MtmFirstViewSet(viewsets.ModelViewSet):

    serializer_class = MtmFirstSerializer
    queryset = MtmFirst.objects.all()


class MtmSecondViewSet(viewsets.ModelViewSet):

    serializer_class = MtmSecondSerializer
    queryset = MtmSecond.objects.all()


class MtoViewSet(viewsets.ModelViewSet):

    serializer_class = MtoSerializer
    queryset = Mto.objects.all()
