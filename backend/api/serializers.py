from django.db import models
from rest_framework import serializers
from items.models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ("name", "description", "price", "stripe_url", "authorized")
