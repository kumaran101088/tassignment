from app.models import Inventory
from rest_framework import status
from .serializers import InventorySerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['DELETE'])
def delete_view(request, pk):
    try:
        product = Inventory.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    product.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['PUT'])
def update_view(request, pk):
    try:
        product = Inventory.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = InventorySerializer(product, data=request.data)
    if serializer.is_valid():
        serializer.validated_data['store']= serializer.validated_data.get('store').upper()
        serializer.validated_data['sku'] = serializer.validated_data.get('sku').lower()
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_AND_REQUEST)