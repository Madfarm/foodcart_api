from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import MenuItem
from .serializers import MenuItemSerializer


@api_view(['GET'])
def getData(request):
    foodCart = {'melon': 3, 'apple': 5, 'banana': 7}
    return Response(foodCart)