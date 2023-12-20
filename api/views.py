from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import MenuItem
from .serializers import MenuItemSerializer


@api_view(['GET' ,'POST'])
def menuItemList(request):
    if request.method == "GET":
            MenuItems = MenuItem.objects.all()
            serializer = MenuItemSerializer(MenuItems, many=True)
    elif request.method == 'POST':
        serializer = MenuItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()


    return Response(serializer.data)


@api_view(['GET'])
def getMenuItem(request, pk):
    data = MenuItem.objects.get(id=pk)
    serializer = MenuItemSerializer(data, many=False)
    return Response(serializer.data)