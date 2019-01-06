from rest_framework import serializers


class WithdrawSerializer(serializers.Serializer):
    money = serializers.IntegerField(required=True, min_value=0)
