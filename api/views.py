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


@api_view(['GET', 'DELETE', 'PUT'])
def getMenuItem(request, pk):
    if request.method == 'DELETE':
        data = MenuItem.objects.get(id=pk)
        data.delete()
        return Response("Item deleted successfully")
    
    elif request.method == 'GET':
        data = MenuItem.objects.get(id=pk)
        serializer = MenuItemSerializer(data, many=False)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        data = MenuItem.objects.get(id=pk)
        serializer = MenuItemSerializer(instance=data, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)