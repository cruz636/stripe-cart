from django.db.models import query
from rest_framework import generics, serializers
from items.models import Item
from .serializers import ItemSerializer

# Create your views here.


class ItemView(generics.ListAPIView):
    queryset = Item.objects.filter(authorized=True)
    serializer_class = ItemSerializer


class DetailItemView(generics.RetrieveAPIView):
    queryset = Item.objects.filter(authorized=True)
    serializer_class = ItemSerializer
