from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from atm.withdraw.withdraw import calculate_change, unroll_change, NoteUnavailableException
from atm.withdraw.serializers import WithdrawSerializer


@api_view(['POST'])
def withdraw(request):
    serializer = WithdrawSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    money = serializer.data['money']
    try:
        change = calculate_change(money)
    except NoteUnavailableException as e:
        raise ValidationError(e)
    unrolled = unroll_change(change)
    return Response(unrolled)
