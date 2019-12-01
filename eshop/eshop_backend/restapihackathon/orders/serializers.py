from rest_framework import serializers
from .models import Order, Component


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'user', 'name', 'components',
                  'orderHash', 'completed')
        # depth  = 1

class OrdersAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'user', 'name', 'components',
                  'orderHash', 'completed')
        depth  = 1        

class ComponentSerializer(serializers.ModelSerializer):
    attributes = serializers.JSONField()

    class Meta:
        model = Component
        fields = ('id', 'componentType', 'name', 'attributes')
        depth = 1
