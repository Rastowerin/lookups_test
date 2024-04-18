from .models import MtmFirst, MtmSecond, Mto
from rest_framework import serializers


class MtmFirstSerializer(serializers.ModelSerializer):

    class Meta:

        model = MtmFirst
        fields = '__all__'


class MtmSecondSerializer(serializers.ModelSerializer):

    class Meta:

        model = MtmSecond
        fields = '__all__'


class MtoSerializer(serializers.ModelSerializer):

    class Meta:

        model = Mto
        fields = '__all__'
