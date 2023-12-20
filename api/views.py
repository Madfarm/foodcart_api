from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import MenuItem
from .serializers import MenuItemSerializer


@api_view(['GET'])
def getData(request):
    MenuItems = MenuItem.objects.all()
    serializer = MenuItemSerializer(MenuItems, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def createMenuItem(request):
    serializer = MenuItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)